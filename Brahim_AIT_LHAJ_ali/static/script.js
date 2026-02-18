/**
 * FoodSafetyScanner — Frontend logic with RAG support
 * Handles drag-and-drop upload, AJAX submission, and rich result rendering
 * including per-ingredient breakdown and RAG statistics.
 */

(() => {
  "use strict";

  // ── DOM refs ──────────────────────────────────────────────────────────
  const dropzone = document.getElementById("dropzone");
  const fileInput = document.getElementById("fileInput");
  const previewArea = document.getElementById("previewArea");
  const previewImg = document.getElementById("previewImg");
  const previewName = document.getElementById("previewName");
  const previewSize = document.getElementById("previewSize");
  const removeBtn = document.getElementById("removeBtn");
  const analyzeBtn = document.getElementById("analyzeBtn");
  const analyzeBtnTxt = document.getElementById("analyzeBtnText");
  const loader = document.getElementById("loader");
  const loaderText = document.getElementById("loaderText");
  const errorCard = document.getElementById("errorCard");
  const resultSection = document.getElementById("resultSection");
  const gaugeNumber = document.getElementById("gaugeNumber");
  const gaugeFill = document.getElementById("gaugeFill");
  const verdictBadge = document.getElementById("verdictBadge");
  const reportText = document.getElementById("reportText");
  const scanAgainBtn = document.getElementById("scanAgainBtn");

  // RAG-specific
  const ragStats = document.getElementById("ragStats");
  const ragTotal = document.getElementById("ragTotal");
  const ragMatched = document.getElementById("ragMatched");
  const ragUnmatched = document.getElementById("ragUnmatched");
  const ingredientsList = document.getElementById("ingredientsList");
  const ingredientsCard = document.getElementById("ingredientsCard");

  let selectedFile = null;
  let loaderInterval = null;

  // ── Helpers ───────────────────────────────────────────────────────────
  const formatBytes = (bytes) => {
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1048576) return (bytes / 1024).toFixed(1) + " KB";
    return (bytes / 1048576).toFixed(1) + " MB";
  };

  const show = (el) => el.classList.add("visible");
  const hide = (el) => el.classList.remove("visible");

  // Loader messages to show the RAG pipeline progress
  const loaderMessages = [
    "Extracting ingredients from label…",
    "Searching ingredient database…",
    "Matching ingredients with knowledge base…",
    "Generating health analysis…",
    "Building your personalized report…",
  ];

  const startLoaderAnimation = () => {
    let idx = 0;
    loaderText.textContent = loaderMessages[0];
    loaderInterval = setInterval(() => {
      idx = (idx + 1) % loaderMessages.length;
      loaderText.style.opacity = "0";
      setTimeout(() => {
        loaderText.textContent = loaderMessages[idx];
        loaderText.style.opacity = "1";
      }, 200);
    }, 2500);
  };

  const stopLoaderAnimation = () => {
    if (loaderInterval) {
      clearInterval(loaderInterval);
      loaderInterval = null;
    }
  };

  // ── File selection ────────────────────────────────────────────────────
  const handleFile = (file) => {
    const allowed = ["image/png", "image/jpeg", "image/jpg", "image/webp"];
    if (!allowed.includes(file.type)) {
      showError("Please upload a PNG, JPG, or WebP image.");
      return;
    }
    if (file.size > 10 * 1024 * 1024) {
      showError("File is too large. Maximum size is 10 MB.");
      return;
    }

    selectedFile = file;

    // Preview
    const reader = new FileReader();
    reader.onload = (e) => {
      previewImg.src = e.target.result;
    };
    reader.readAsDataURL(file);

    previewName.textContent = file.name;
    previewSize.textContent = formatBytes(file.size);
    show(previewArea);
    dropzone.style.display = "none";
    hide(errorCard);
    hide(resultSection);
  };

  // Drag & drop events
  ["dragenter", "dragover"].forEach((evt) => {
    dropzone.addEventListener(evt, (e) => {
      e.preventDefault();
      dropzone.classList.add("drag-over");
    });
  });

  ["dragleave", "drop"].forEach((evt) => {
    dropzone.addEventListener(evt, (e) => {
      e.preventDefault();
      dropzone.classList.remove("drag-over");
    });
  });

  dropzone.addEventListener("drop", (e) => {
    const files = e.dataTransfer.files;
    if (files.length) handleFile(files[0]);
  });

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length) handleFile(fileInput.files[0]);
  });

  // Remove preview
  removeBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    selectedFile = null;
    fileInput.value = "";
    hide(previewArea);
    dropzone.style.display = "";
  });

  // ── Error display ─────────────────────────────────────────────────────
  const showError = (msg) => {
    errorCard.textContent = msg;
    show(errorCard);
    hide(loader);
    stopLoaderAnimation();
    analyzeBtn.disabled = false;
    analyzeBtnTxt.textContent = "Analyze Label";
  };

  // ── Score colour ──────────────────────────────────────────────────────
  const scoreColor = (score) => {
    if (score >= 7) return "hsl(142, 71%, 40%)";   // green
    if (score >= 4) return "hsl(38, 92%, 50%)";     // amber
    return "hsl(0, 84%, 60%)";                      // red
  };

  const verdictClass = (score) => {
    if (score >= 7) return "verdict-badge--good";
    if (score >= 4) return "verdict-badge--moderate";
    return "verdict-badge--bad";
  };

  // ── Risk level helpers ────────────────────────────────────────────────
  const riskIcon = (risk) => {
    switch ((risk || "").toLowerCase()) {
      case "good": return "✅";
      case "moderate": return "⚠️";
      case "bad": return "🚫";
      default: return "ℹ️";
    }
  };

  const riskClass = (risk) => {
    switch ((risk || "").toLowerCase()) {
      case "good": return "ingredient-item--good";
      case "moderate": return "ingredient-item--moderate";
      case "bad": return "ingredient-item--bad";
      default: return "ingredient-item--neutral";
    }
  };

  // ── Gauge animation ──────────────────────────────────────────────────
  const CIRCUMFERENCE = 2 * Math.PI * 65;

  const setGauge = (score) => {
    const pct = score / 10;
    const offset = CIRCUMFERENCE * (1 - pct);
    gaugeFill.style.strokeDasharray = CIRCUMFERENCE;
    gaugeFill.style.strokeDashoffset = CIRCUMFERENCE;
    gaugeFill.style.stroke = scoreColor(score);

    void gaugeFill.getBoundingClientRect();

    requestAnimationFrame(() => {
      gaugeFill.style.strokeDashoffset = offset;
    });

    // Animate number
    let current = 0;
    const step = () => {
      current += 0.2;
      if (current > score) current = score;
      gaugeNumber.textContent = Math.round(current);
      gaugeNumber.style.color = scoreColor(score);
      if (current < score) requestAnimationFrame(step);
    };
    step();
  };

  // ── Render ingredients breakdown ─────────────────────────────────────
  const renderIngredients = (details) => {
    ingredientsList.innerHTML = "";

    if (!details || !details.length) {
      ingredientsCard.style.display = "none";
      return;
    }

    ingredientsCard.style.display = "block";

    details.forEach((item, i) => {
      const div = document.createElement("div");
      div.className = `ingredient-item ${riskClass(item.risk_level)}`;
      div.style.animationDelay = `${i * 0.05}s`;

      div.innerHTML = `
        <div class="ingredient-item__header">
          <span class="ingredient-item__icon">${riskIcon(item.risk_level)}</span>
          <span class="ingredient-item__name">${item.name}</span>
          <span class="ingredient-item__badge ingredient-item__badge--${(item.risk_level || "neutral").toLowerCase()}">${item.risk_level || "unknown"}</span>
        </div>
        <div class="ingredient-item__meta">
          <span class="ingredient-item__category">${item.category || ""}</span>
          <span class="ingredient-item__effect">${item.effect || ""}</span>
        </div>
      `;

      ingredientsList.appendChild(div);
    });
  };

  // ── Render RAG stats ─────────────────────────────────────────────────
  const renderRagStats = (stats) => {
    if (!stats) {
      ragStats.style.display = "none";
      return;
    }
    ragStats.style.display = "flex";
    animateNumber(ragTotal, stats.total_ingredients_found || 0);
    animateNumber(ragMatched, stats.matched_in_database || 0);
    animateNumber(ragUnmatched, stats.not_in_database || 0);
  };

  const animateNumber = (el, target) => {
    let current = 0;
    const step = () => {
      current++;
      if (current > target) current = target;
      el.textContent = current;
      if (current < target) requestAnimationFrame(step);
    };
    step();
  };

  // ── Analyze ───────────────────────────────────────────────────────────
  analyzeBtn.addEventListener("click", async () => {
    if (!selectedFile) {
      showError("Please upload an image first.");
      return;
    }

    hide(errorCard);
    hide(resultSection);
    show(loader);
    startLoaderAnimation();
    analyzeBtn.disabled = true;
    analyzeBtnTxt.textContent = "Analyzing…";

    const formData = new FormData();
    formData.append("image", selectedFile);

    // 2-minute timeout for the two-pass RAG pipeline
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 120_000);

    try {
      const res = await fetch("/analyze", {
        method: "POST",
        body: formData,
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      let data;
      const rawText = await res.text();
      try {
        data = JSON.parse(rawText);
      } catch (parseErr) {
        showError("Server returned invalid data. Raw: " + rawText.slice(0, 200));
        return;
      }

      if (!res.ok || data.error) {
        showError(data.error || "Something went wrong. Try again.");
        return;
      }

      // Populate results
      setGauge(data.score);

      verdictBadge.textContent = data.verdict;
      verdictBadge.className = "verdict-badge " + verdictClass(data.score);

      reportText.textContent = data.report;

      // RAG-specific rendering
      renderRagStats(data.rag_stats);
      renderIngredients(data.ingredients_detail);

      hide(loader);
      stopLoaderAnimation();
      show(resultSection);
      analyzeBtn.disabled = false;
      analyzeBtnTxt.textContent = "Analyze Label";

      // Smooth scroll to result
      resultSection.scrollIntoView({ behavior: "smooth", block: "start" });

    } catch (err) {
      clearTimeout(timeoutId);
      if (err.name === "AbortError") {
        showError("Request timed out. The analysis is taking too long — please try a clearer image.");
      } else {
        showError("Network error: " + err.message + ". Check that the server is running.");
      }
    }
  });

  // ── Scan Again ────────────────────────────────────────────────────────
  scanAgainBtn.addEventListener("click", () => {
    selectedFile = null;
    fileInput.value = "";
    hide(previewArea);
    dropzone.style.display = "";
    hide(resultSection);
    hide(errorCard);
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
})();
