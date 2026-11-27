# 🥦 FoodSafetyScanner — AI-Powered Food Label Analysis

**FoodSafetyScanner** is a sophisticated web application designed to help consumers make healthier food choices. By simply uploading a photo of a food product label, the application uses **Retrieval-Augmented Generation (RAG)** and **Google Gemini AI** to provide an instant, science-grounded health report.

![Banner](https://img.shields.io/badge/AI-Gemini-blue?style=for-the-badge&logo=google-gemini)
![Banner](https://img.shields.io/badge/Backend-Flask-lightgrey?style=for-the-badge&logo=flask)
![Banner](https://img.shields.io/badge/RAG-Database-green?style=for-the-badge&logo=json)

---

## ✨ Features

- **🔍 Intelligent Extraction**: Automatically detects and extracts every ingredient from your food label photos using Gemini Vision.
- **🧠 RAG-Enhanced Analysis**: Matches extracted ingredients against a curated knowledge base of over 100+ ingredients to provide factual health data.
- **📊 Health Scoring**: Generates a health score from 0 to 10 with a clear verdict (Healthy, Moderate, or Unhealthy).
- **📝 Detailed Reports**: Provides a comprehensive breakdown of each ingredient's category, effects, and individual risk level.
- **🎨 Premium UI**: A modern, responsive interface with glassmorphism effects and smooth animations.

---

## 🚀 Tech Stack

- **Backend**: Python 3.x + [Flask](https://flask.palletsprojects.com/)
- **AI Core**: [Google Generative AI (Gemini)](https://ai.google.dev/)
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Data Engine**: JSON-based Retrieval-Augmented Generation (RAG)
- **Environment**: Dotenv for secure API management

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AIT-LHAJ-ALI-BRAHIM/FoodSafetyScanner.git
cd FoodSafetyScanner
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API Key:
```env
# Get your key at https://aistudio.google.com/
GOOGLE_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
```bash
python app.py
```
Open `http://localhost:5000` in your browser.

---

## 🧠 How it Works (RAG Architecture)

1. **Pass 1 (Vision)**: Gemini Vision analyzes the uploaded image to extract a raw list of ingredient names.
2. **Retrieval**: The system performs a fuzzy-match search against `data.json` to find detailed health data for those ingredients.
3. **Pass 2 (Grounding)**: The system sends both the *extracted names* and the *retrieved factual data* back to Gemini. This prevents "hallucinations" and ensures the report is based on verified information.
4. **Rendering**: The frontend receives a structured JSON response and builds the dynamic UI cards and score gauge.

---

## 📂 Project Structure

```text
├── app.py              # Flask server & RAG logic
├── data.json           # Ingredient knowledge base
├── .env                # API Keys (gitignored)
├── requirements.txt    # Python dependencies
├── static/
│   ├── script.js       # Frontend interaction & rendering
│   └── style.css       # Premium styles and animations
└── templates/
    └── index.html      # Main application structure
```

---

## 📄 License

This project is built for educational and personal health awareness purposes. 
*Disclaimer: This app provides AI-generated analysis and should not replace professional medical or nutritional advice.*

---
Built with 💚 by **Brahim**
