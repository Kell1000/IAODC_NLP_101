"""
FoodSafetyScanner — Flask backend with RAG (Retrieval-Augmented Generation).
Uses data.json as a curated ingredient knowledge base:
  1. Gemini Vision extracts ingredient names from the label image.
  2. Ingredients are fuzzy-matched against data.json (local retrieval).
  3. Matched knowledge is sent back to Gemini for a grounded health report.
"""

import os
import json
import re
import traceback
from difflib import SequenceMatcher

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. "
        "Copy .env.example to .env and add your key."
    )

genai.configure(api_key=GOOGLE_API_KEY)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

# ---------------------------------------------------------------------------
# Load ingredient knowledge base (data.json)
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    INGREDIENT_DB = json.load(f)

# Build a lookup dict: normalised name → full record
INGREDIENT_LOOKUP = {}
for entry in INGREDIENT_DB:
    key = entry["ingredient"].lower().strip()
    INGREDIENT_LOOKUP[key] = entry

print(f"[RAG] Loaded {len(INGREDIENT_DB)} ingredients into knowledge base.")

# ---------------------------------------------------------------------------
# Flask app
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


# Ensure Flask errors return JSON (not HTML that breaks fetch)
@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "File is too large. Maximum size is 10 MB."}), 413


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": f"Server error: {str(e)}"}), 500

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

# Pass 1: Extract ingredients from label image
EXTRACT_PROMPT = (
    "Look at this food product label image carefully. "
    "Extract EVERY ingredient listed on the label. "
    "Return ONLY a raw JSON array of ingredient name strings. "
    "Do not use markdown formatting like ```json. "
    "Example output: [\"Water\", \"Sugar\", \"Salt\", \"Citric Acid\"]\n\n"
    "Rules:\n"
    "- Extract each ingredient as a separate string\n"
    "- Use the exact names as written on the label\n"
    "- Include sub-ingredients in parentheses as separate entries too\n"
    "- If you cannot read any ingredients, return an empty array []\n"
)

# Pass 2: Generate health report using retrieved knowledge
def build_analysis_prompt(ingredients_from_label, matched_knowledge, unmatched_names):
    """Build the augmented prompt with retrieved ingredient data."""
    knowledge_block = ""
    if matched_knowledge:
        knowledge_block = "## INGREDIENT KNOWLEDGE BASE (verified data):\n"
        for item in matched_knowledge:
            knowledge_block += (
                f"- **{item['ingredient']}** | Category: {item['category']} | "
                f"Effect: {item['effect_summary']} | "
                f"Detail: {item['health_effect']}\n"
            )
        knowledge_block += "\n"

    unmatched_block = ""
    if unmatched_names:
        unmatched_block = (
            "## INGREDIENTS NOT IN DATABASE (use your general knowledge):\n"
            f"{', '.join(unmatched_names)}\n\n"
        )

    prompt = (
        "You are a food safety expert. Analyze the following ingredients found on "
        "a food product label.\n\n"
        f"## INGREDIENTS FROM LABEL:\n{', '.join(ingredients_from_label)}\n\n"
        f"{knowledge_block}"
        f"{unmatched_block}"
        "Using the INGREDIENT KNOWLEDGE BASE above as your PRIMARY source of truth, "
        "and your general knowledge for any ingredients not in the database, "
        "provide a health analysis.\n\n"
        "Return ONLY raw JSON (no markdown fences). Use this exact structure:\n"
        "{\n"
        '  "score": <integer 0-10, 10 = healthiest>,\n'
        '  "verdict": "<Healthy, Moderate Risk, or Unhealthy>",\n'
        '  "report": "<5-7 line paragraph explaining the overall health impact, '
        'mentioning key good and bad ingredients with their effects>",\n'
        '  "ingredients_detail": [\n'
        "    {\n"
        '      "name": "<ingredient name>",\n'
        '      "category": "<category>",\n'
        '      "effect": "<brief effect summary>",\n'
        '      "risk_level": "<good, moderate, or bad>"\n'
        "    }\n"
        "  ]\n"
        "}\n\n"
        "IMPORTANT:\n"
        "- The 'ingredients_detail' array should cover EVERY ingredient from the label\n"
        "- Use the knowledge base data when available — do not contradict it\n"
        "- For ingredients NOT in the database, use your general knowledge\n"
        "- Be honest and science-based in your assessment\n"
    )
    return prompt


# ---------------------------------------------------------------------------
# RAG: Fuzzy matching engine
# ---------------------------------------------------------------------------
def fuzzy_match_ingredient(name, threshold=0.65):
    """
    Match an extracted ingredient name against the knowledge base.
    Uses exact match first, then fuzzy substring/sequence matching.
    Returns the matched record or None.
    """
    normalised = name.lower().strip()

    # 1. Exact match
    if normalised in INGREDIENT_LOOKUP:
        return INGREDIENT_LOOKUP[normalised]

    # 2. Check if any DB key is contained in the name, or vice versa
    for key, record in INGREDIENT_LOOKUP.items():
        # Substring containment (either direction)
        if key in normalised or normalised in key:
            return record

    # 3. Fuzzy sequence matching
    best_score = 0
    best_record = None
    for key, record in INGREDIENT_LOOKUP.items():
        score = SequenceMatcher(None, normalised, key).ratio()
        if score > best_score:
            best_score = score
            best_record = record

    if best_score >= threshold:
        return best_record

    return None


def retrieve_knowledge(ingredient_names):
    """
    Given a list of ingredient names from the label,
    retrieve matching records from data.json.
    Returns (matched_records, unmatched_names).
    """
    matched = []
    unmatched = []
    seen_ids = set()

    for name in ingredient_names:
        record = fuzzy_match_ingredient(name)
        if record and record["id"] not in seen_ids:
            matched.append(record)
            seen_ids.add(record["id"])
        elif record is None:
            unmatched.append(name)

    return matched, unmatched


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def _parse_json_response(raw_text):
    """Robustly extract JSON from Gemini's response."""
    # 1. Try stripping ```json ... ``` fences
    fence_match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", raw_text, re.DOTALL)
    if fence_match:
        json_str = fence_match.group(1).strip()
    else:
        # 2. Try to find a JSON object or array anywhere in the text
        brace_match = re.search(r"[\{\[].*[\}\]]", raw_text, re.DOTALL)
        if brace_match:
            json_str = brace_match.group(0).strip()
        else:
            json_str = raw_text

    return json.loads(json_str)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """
    RAG-powered analysis:
      1. Extract ingredients from label via Gemini Vision
      2. Retrieve matching knowledge from data.json
      3. Generate grounded health report via Gemini
    """

    if "image" not in request.files:
        return jsonify({"error": "No image file provided."}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    if not _allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type. Use PNG, JPG, JPEG, or WEBP."}), 400

    try:
        # Read image bytes
        image_bytes = file.read()
        mime_type = file.content_type or "image/jpeg"

        image_part = {
            "mime_type": mime_type,
            "data": image_bytes,
        }

        model = genai.GenerativeModel("gemini-2.5-flash")

        # ── PASS 1: Extract ingredients from the image ──────────────────
        print("[RAG] Pass 1: Extracting ingredients from label...")
        extract_response = model.generate_content(
            [EXTRACT_PROMPT, image_part],
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=2048,
                response_mime_type="application/json",
            ),
        )

        raw_extract = extract_response.text.strip()
        print(f"[RAG] Extracted raw: {raw_extract[:500]}")

        ingredients_list = _parse_json_response(raw_extract)

        if not isinstance(ingredients_list, list):
            ingredients_list = []

        # Clean up: ensure all items are strings
        ingredients_list = [str(i).strip() for i in ingredients_list if i]
        print(f"[RAG] Found {len(ingredients_list)} ingredients: {ingredients_list}")

        # ── RETRIEVAL: Match against data.json ──────────────────────────
        matched_records, unmatched_names = retrieve_knowledge(ingredients_list)
        print(
            f"[RAG] Matched: {len(matched_records)} | "
            f"Unmatched: {len(unmatched_names)} ({unmatched_names})"
        )

        # ── PASS 2: Generate grounded health report ─────────────────────
        analysis_prompt = build_analysis_prompt(
            ingredients_list, matched_records, unmatched_names
        )
        print("[RAG] Pass 2: Generating augmented health report...")

        analysis_response = model.generate_content(
            [analysis_prompt, image_part],
            generation_config=genai.types.GenerationConfig(
                temperature=0.3,
                max_output_tokens=4096,
                response_mime_type="application/json",
            ),
        )

        raw_analysis = analysis_response.text.strip()
        print(f"[RAG] Analysis raw: {raw_analysis[:500]}")

        result = _parse_json_response(raw_analysis)

        # Validate required fields
        if "score" not in result or "verdict" not in result or "report" not in result:
            return jsonify({"error": "Gemini returned incomplete data. Please try again."}), 502

        result["score"] = max(0, min(10, int(result["score"])))

        # Add RAG metadata to the response
        result["rag_stats"] = {
            "total_ingredients_found": len(ingredients_list),
            "matched_in_database": len(matched_records),
            "not_in_database": len(unmatched_names),
            "ingredients_extracted": ingredients_list,
        }

        return jsonify(result)

    except json.JSONDecodeError:
        return jsonify({"error": f"Failed to parse response. Raw: {raw_analysis[:500]}"}), 502
    except Exception as exc:
        traceback.print_exc()
        return jsonify({"error": f"Analysis failed: {str(exc)}"}), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
