#  Krishi Mitra (कृषि मित्र) — Autonomous Agricultural AI Extension Agent

[![CI](https://github.com/pratyayroy007/KrishiMitra/actions/workflows/ci.yml/badge.svg)](https://github.com/pratyayroy007/KrishiMitra/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![PyTorch](https://img.shields.io/badge/Vision-PyTorch%20MobileNetV2-red.svg)](https://pytorch.org/)
[![Gemini 3.8 Flash](https://img.shields.io/badge/Copilot-Gemini%203.8%20Flash-orange.svg)](https://ai.google.dev/)
[![Open-Meteo](https://img.shields.io/badge/Climate-Open--Meteo%20API-yellow.svg)](https://open-meteo.com/)
[![Languages](https://img.shields.io/badge/Vernacular-6%20Indian%20Languages-purple.svg)](#-pillar-4-regional-languages--vernacular-voice-assistant)

**Krishi Mitra** is an end-to-end AI-powered Agricultural Extension platform designed to bridge the digital divide for smallholder farmers across India. Grounded on scientific recommendations from the **Indian Council of Agricultural Research (ICAR)** and state Agricultural Universities, Krishi Mitra provides hyper-local crop recommendation, real-time leaf optical disease detection, grounded conversational advisory, and vernacular multi-language voice assistance.

---

##  The 4 Core System Pillars

### 1.  Pillar 1: Multi-Crop Recommendation Engine
- **Model**: Machine Learning Random Forest classifier.
- **Inputs**: Soil Chemistry ($N, P, K$, soil $\text{pH}$) combined with atmospheric factors (temperature, relative humidity, growing rainfall).
- **Hyper-Local Climate Integration**: Direct real-time GPS & district weather queries powered by **Open-Meteo API** (zero API keys required). Auto-fills live temperature, humidity, and rainfall into prediction forms with a single click.

### 2.  Pillar 2: Real-Time Field Leaf Disease Detection (Computer Vision)
- **Deep Learning Model**: Lightweight **MobileNetV2** neural network trained on **19–20 plant pathology classes**.
- **Supported Crops**: Rice, Potato, Tomato, Maize/Corn, Apple, Grape, Peach, Bell Pepper.
- **Diagnostics**: Detects pathogens including Rice Blast, Potato Late Blight, Tomato Early Blight, Apple Scab, and Black Rot.
- **Standalone CPU Inference**: Ultra-low latency (~25ms CPU inference) requiring no external drives or GPU instances.
- **Prescriptive Output**: Instant actionable ICAR-approved chemical fungicides, dosages (e.g. Mancozeb, Tricyclazole), organic biocontrol options, and cultural prevention measures.

### 3.  Pillar 3: Grounded Agronomic Advisory Copilot
- **AI Core**: **Google Gemini 3.8 Flash** with system prompts grounded on ICAR Package-of-Practices (PoP).
- **Offline Zero-Latency Fail-Safe**: Built-in ICAR Agronomic Knowledge Base with a timeout protector guaranteeing instant fallback advice for critical crop issues even with zero internet connectivity.
- **Context-Aware Recommendations**: Integrates active crop context (e.g. recommended crops or diagnosed leaves) directly into conversational advice.

### 4.  Pillar 4: Regional Languages & Vernacular Voice Assistant
- **6 Supported Languages**:
  - 🇬🇧 English (`en`, `en-IN`)
  - 🇮🇳 हिन्दी (Hindi - `hi`, `hi-IN`)
  - 🇮🇳 বাংলা (Bengali - `bn`, `bn-IN`)
  - 🇮🇳 తెలుగు (Telugu - `te`, `te-IN`)
  - 🇮🇳 मराठी (Marathi - `mr`, `mr-IN`)
  - 🇮🇳 தமிழ் (Tamil - `ta`, `ta-IN`)
- **Zero-Reload Dynamic UI**: Full-stack dynamic localization across the navbar, weather cards, forms, and results.
- ** Speech-to-Text (STT)**: Web Speech API microphone input enabling farmers to speak queries naturally in their mother tongue.
- ** High-Fidelity Text-to-Speech (TTS) Streaming**: Dedicated `/api/tts` endpoint delivering fluent, native-accented audio readouts for:
  - Global Voice Guide walkthroughs
  - Live weather & spraying window advisories
  - Crop prediction rationale
  - Leaf disease diagnosis & fungicide recipes
  - AI Copilot responses with optional **Auto-Voice Readout**.

---

##  Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend & APIs** | Python 3.10+, Flask, Requests, ThreadPoolExecutor |
| **Machine Learning** | Scikit-learn, Pandas, NumPy, Joblib |
| **Computer Vision** | PyTorch, Torchvision (MobileNetV2), Pillow |
| **Generative AI** | Google GenAI SDK (`gemini-3.8-flash`), ICAR PoP Knowledge Base |
| **Agro-Meteorology** | Open-Meteo Live API, Open-Meteo Geocoding API |
| **Frontend UI/UX** | HTML5, Modern CSS3 (Glassmorphism, Dark Agricultural Theme), JavaScript ES6+ |
| **Voice & Speech** | Web Speech API (`SpeechRecognition`), High-Fidelity TTS Streamer (`/api/tts`) |

---

##  Project Structure

```text
krishimitra/
├── app.py                     # Main Flask application & API routes
├── run.bat                    # One-click Windows launch script
├── requirements.txt           # Project dependencies
├── test_disease_model.py      # Standalone verification script for CV disease detection
├── test_regional_languages.py # Automated unit test suite for multilingual APIs
│
├── model/
│   ├── crop_model.pkl         # Trained Random Forest crop recommendation model
│   ├── best_plant_disease_model.pth # PyTorch MobileNetV2 disease detection weights
│   └── class_names.json       # 19-class plant disease taxonomy mapping
│
├── services/
│   ├── chatbot_service.py     # Gemini 3.8 Flash copilot & ICAR PoP knowledge base
│   ├── disease_service.py     # MobileNetV2 leaf inference & diagnosis pipeline
│   ├── translation_service.py # Multilingual agronomic dictionaries (6 languages)
│   └── weather_service.py     # Open-Meteo live agro-climate & spraying advisory engine
│
├── static/
│   ├── css/
│   │   └── style.css          # Modern UI stylesheet with voice & responsive HUD components
│   ├── js/
│   │   └── translations.js    # Regional language dictionaries & KrishiVoiceEngine
│   └── images/
│
├── templates/
│   ├── index.html             # Main responsive single-page application
│   └── result.html
│
└── screenshots/               # Project interface previews and diagrams
```

---

##  Quick Start & Installation

### Prerequisites
- Python 3.10, 3.11, or 3.12 installed
- Modern Chromium browser (Google Chrome, Microsoft Edge, Brave)

### 1. Clone the Repository
```bash
git clone https://github.com/pratyayroy007/KrishiMitra.git
cd KrishiMitra
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
#### Option A: One-Click Launch (Windows)
Double-click `run.bat` in the project root.

#### Option B: Terminal
```bash
python app.py
```

### 4. Open in Browser
Navigate to:
```text
http://127.0.0.1:5000
```

---

##  Testing & Verification

Run the automated test suites to verify system modules:

```bash
# Test regional language translations & multilingual API endpoints
python test_regional_languages.py

# Test Computer Vision disease classification
python test_disease_model.py hi
```

---

##  Academic Attribution & TARP Project

Developed as part of the **Final Year Technology Applied Research Project (TARP)**. Grounded on agronomic guidelines formulated by the **Indian Council of Agricultural Research (ICAR)** and regional State Agricultural Universities (SAUs).
