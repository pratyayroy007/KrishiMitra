import os
import pickle
import numpy as np
import pandas as pd
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from services.chatbot_service import copilot_service
from services.disease_service import disease_service
from services.weather_service import weather_service

app = Flask(__name__)

# Load trained crop recommendation model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'crop_model.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

FEATURE_COLUMNS = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    form_data = {
        'N': '', 'P': '', 'K': '',
        'temperature': '', 'humidity': '', 'ph': '', 'rainfall': ''
    }

    if request.method == 'POST':
        try:
            form_data = {
                'N': request.form.get('N', ''),
                'P': request.form.get('P', ''),
                'K': request.form.get('K', ''),
                'temperature': request.form.get('temperature', ''),
                'humidity': request.form.get('humidity', ''),
                'ph': request.form.get('ph', ''),
                'rainfall': request.form.get('rainfall', '')
            }

            features_df = pd.DataFrame([[
                float(form_data['N']),
                float(form_data['P']),
                float(form_data['K']),
                float(form_data['temperature']),
                float(form_data['humidity']),
                float(form_data['ph']),
                float(form_data['rainfall'])
            ]], columns=FEATURE_COLUMNS)

            raw_pred = model.predict(features_df)[0]
            prediction = str(raw_pred).capitalize()
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction, form_data=form_data)


# -------------------------------------------------------------
# 🤖 CHATBOT MODULE (Adapted from Caterpillar AI Copilot)
# -------------------------------------------------------------
@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.get_json(silent=True) or {}
    query = data.get('query', '')
    crop_context = data.get('crop_context', None)
    lang = data.get('lang', 'en')

    if not query:
        return jsonify({"error": "Empty query"}), 400

    result = copilot_service.answer_query(query=query, crop_context=crop_context, lang=lang)
    return jsonify(result)


# -------------------------------------------------------------
# 📷 CAMERA & DISEASE DETECTION MODULE (Adapted from Caterpillar Optical Monitor)
# -------------------------------------------------------------
@app.route('/api/scan_leaf', methods=['POST'])
def api_scan_leaf():
    data = request.get_json(silent=True) or {}
    image_b64 = data.get('image', '')
    lang = data.get('lang', 'en')

    if not image_b64:
        return jsonify({"status": "error", "message": "No image provided"}), 400

    result = disease_service.analyze_image_base64(image_b64, lang=lang)
    return jsonify(result)


# -------------------------------------------------------------
# ⛅ LIVE WEATHER INTEGRATION (Open-Meteo & Geocoding)
# -------------------------------------------------------------
@app.route('/api/weather', methods=['GET'])
def api_weather():
    city = request.args.get('city', None)
    lat = request.args.get('lat', None, type=float)
    lon = request.args.get('lon', None, type=float)

    result = weather_service.get_weather(city=city, lat=lat, lon=lon)
    status_code = 200 if result.get('status') == 'success' else 400
    return jsonify(result), status_code


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)