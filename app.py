import os
import pickle
import numpy as np
import pandas as pd
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

# Import the integrated Copilot and Disease Detection services
from services.chatbot_service import copilot_service
from services.disease_service import disease_service

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

    if not query:
        return jsonify({"error": "Empty query"}), 400

    result = copilot_service.answer_query(query=query, crop_context=crop_context)
    return jsonify(result)


# -------------------------------------------------------------
# 📷 CAMERA & DISEASE DETECTION MODULE (Adapted from Caterpillar Optical Monitor)
# -------------------------------------------------------------
@app.route('/api/scan_leaf', methods=['POST'])
def api_scan_leaf():
    data = request.get_json(silent=True) or {}
    image_b64 = data.get('image', '')

    if not image_b64:
        return jsonify({"status": "error", "message": "No image provided"}), 400

    result = disease_service.analyze_image_base64(image_b64)
    return jsonify(result)


# -------------------------------------------------------------
# ⛅ LIVE WEATHER INTEGRATION (Open-Meteo & Geocoding)
# -------------------------------------------------------------
@app.route('/api/weather', methods=['GET'])
def api_weather():
    city = request.args.get('city', '').strip()
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')

    try:
        # If city name is provided, geocode it
        if city and (not lat or not lon):
            geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
            geo_res = requests.get(geo_url, timeout=5).json()
            if not geo_res.get('results'):
                return jsonify({"error": f"City '{city}' not found"}), 404
            lat = geo_res['results'][0]['latitude']
            lon = geo_res['results'][0]['longitude']
            city_name = geo_res['results'][0]['name']
        else:
            city_name = "Detected Location"

        if not lat or not lon:
            return jsonify({"error": "Latitude/Longitude or City required"}), 400

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,precipitation&timezone=auto"
        )
        w_res = requests.get(weather_url, timeout=5).json()
        current = w_res.get('current', {})

        return jsonify({
            "status": "success",
            "city": city_name,
            "latitude": lat,
            "longitude": lon,
            "temperature": current.get('temperature_2m', 25.0),
            "humidity": current.get('relative_humidity_2m', 65.0),
            "rainfall": current.get('precipitation', 100.0)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)