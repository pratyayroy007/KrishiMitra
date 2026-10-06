"""Krishi Mitra Agro-Weather Service
Powered by Open-Meteo (Lightweight, Keyless, Real-Time Climate API)
Provides:
- Instant geocoding for Indian cities and districts
- Real-time temperature, humidity, rainfall, wind speed, WMO weather codes
- 5-day agro-meteorological forecast
- Smart Farming Advisory (Spraying safety, Irrigation schedule)
"""

import logging
import requests
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

WMO_WEATHER_CODES = {
    0: {"desc": "Clear Sky", "icon": "☀️"},
    1: {"desc": "Mainly Clear", "icon": "🌤️"},
    2: {"desc": "Partly Cloudy", "icon": "⛅"},
    3: {"desc": "Overcast", "icon": "☁️"},
    45: {"desc": "Foggy", "icon": "🌫️"},
    48: {"desc": "Depositing Rime Fog", "icon": "🌫️"},
    51: {"desc": "Light Drizzle", "icon": "🌦️"},
    53: {"desc": "Moderate Drizzle", "icon": "🌦️"},
    55: {"desc": "Dense Drizzle", "icon": "🌧️"},
    61: {"desc": "Slight Rain", "icon": "🌧️"},
    63: {"desc": "Moderate Rain", "icon": "🌧️"},
    65: {"desc": "Heavy Rain", "icon": "⛈️"},
    71: {"desc": "Slight Snow Fall", "icon": "🌨️"},
    73: {"desc": "Moderate Snow Fall", "icon": "🌨️"},
    75: {"desc": "Heavy Snow Fall", "icon": "❄️"},
    80: {"desc": "Slight Rain Showers", "icon": "🌦️"},
    81: {"desc": "Moderate Rain Showers", "icon": "🌧️"},
    82: {"desc": "Violent Rain Showers", "icon": "⛈️"},
    95: {"desc": "Thunderstorm", "icon": "⛈️"},
    96: {"desc": "Thunderstorm with Slight Hail", "icon": "⛈️"},
    99: {"desc": "Thunderstorm with Heavy Hail", "icon": "⛈️"},
}


class OpenMeteoWeatherService:
    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, city: Optional[str] = None, lat: Optional[float] = None, lon: Optional[float] = None) -> Dict[str, Any]:
        """Fetches current conditions, 5-day forecast, and agricultural advisory."""
        try:
            city_name = "Detected Region"
            admin_region = ""

            # 1. Geocode if city name provided
            if city and (lat is None or lon is None):
                geo_resp = requests.get(
                    self.GEO_URL,
                    params={"name": city.strip(), "count": 1, "language": "en", "format": "json"},
                    timeout=5
                ).json()

                results = geo_resp.get("results")
                if not results:
                    return {"status": "error", "message": f"City or district '{city}' not found."}

                top_hit = results[0]
                lat = top_hit["latitude"]
                lon = top_hit["longitude"]
                city_name = top_hit.get("name", city)
                admin_region = top_hit.get("admin1", "")
            elif lat is not None and lon is not None:
                city_name = f"{lat:.2f}°, {lon:.2f}°"

            if lat is None or lon is None:
                return {"status": "error", "message": "Latitude/Longitude or valid City required."}

            # 2. Call Open-Meteo Forecast API
            weather_resp = requests.get(
                self.FORECAST_URL,
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,relative_humidity_2m,precipitation,weather_code,wind_speed_10m",
                    "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum",
                    "timezone": "auto"
                },
                timeout=5
            ).json()

            current = weather_resp.get("current", {})
            daily = weather_resp.get("daily", {})

            temp = current.get("temperature_2m", 25.0)
            humidity = current.get("relative_humidity_2m", 65.0)
            precip = current.get("precipitation", 0.0)
            w_code = current.get("weather_code", 0)
            wind = current.get("wind_speed_10m", 5.0)

            w_info = WMO_WEATHER_CODES.get(w_code, {"desc": "Partly Cloudy", "icon": "⛅"})

            # 3. Build 5-Day Forecast Array
            forecast_days = []
            dates = daily.get("time", [])[:5]
            max_temps = daily.get("temperature_2m_max", [])[:5]
            min_temps = daily.get("temperature_2m_min", [])[:5]
            rain_sums = daily.get("precipitation_sum", [])[:5]
            codes = daily.get("weather_code", [])[:5]

            total_rain_next_3_days = sum(rain_sums[:3]) if len(rain_sums) >= 3 else 0.0

            for i in range(len(dates)):
                day_code = codes[i] if i < len(codes) else 0
                day_info = WMO_WEATHER_CODES.get(day_code, {"desc": "Clear", "icon": "☀️"})
                forecast_days.append({
                    "date": dates[i],
                    "max_temp": max_temps[i] if i < len(max_temps) else temp,
                    "min_temp": min_temps[i] if i < len(min_temps) else temp - 5,
                    "rain_mm": rain_sums[i] if i < len(rain_sums) else 0.0,
                    "desc": day_info["desc"],
                    "icon": day_info["icon"]
                })

            # 4. Generate Farmer Advisory
            advisory = self._generate_agri_advisory(temp, humidity, precip, total_rain_next_3_days, wind)

            # Heuristic seasonal rainfall for crop recommendation form
            # If current precip is 0, estimate standard growing rainfall from humidity & rain sums
            model_rainfall = round(max(precip * 20.0, total_rain_next_3_days * 15.0, humidity * 1.8), 1)

            return {
                "status": "success",
                "city": city_name,
                "admin_region": admin_region,
                "latitude": lat,
                "longitude": lon,
                "temperature": round(temp, 1),
                "humidity": round(humidity, 1),
                "rainfall": model_rainfall,
                "live_precipitation": precip,
                "wind_speed_kmh": round(wind, 1),
                "weather_desc": w_info["desc"],
                "weather_icon": w_info["icon"],
                "forecast": forecast_days,
                "advisory": advisory
            }

        except Exception as e:
            logger.error(f"Open-Meteo service error: {e}")
            return {"status": "error", "message": f"Failed to retrieve weather data: {str(e)}"}

    def _generate_agri_advisory(self, temp: float, humidity: float, precip: float, rain_3d: float, wind: float) -> Dict[str, str]:
        # Spraying safety
        if rain_3d > 3.0 or precip > 0.5:
            spray_status = "⚠️ Delay Spraying"
            spray_msg = "Rain expected in the next 48-72 hours. Fungicides and pesticides may be washed away."
        elif wind > 20.0:
            spray_status = "⚠️ High Wind Drift"
            spray_msg = f"Wind speed ({wind} km/h) is too high for uniform droplet deposition. Spray during dawn or dusk."
        else:
            spray_status = "✅ Favorable for Spraying"
            spray_msg = "Low wind and clear conditions. Ideal window for foliar sprays and fertilizers."

        # Irrigation recommendation
        if rain_3d > 10.0:
            irrigation_status = "🌧️ Postpone Irrigation"
            irrigation_msg = f"Substantial rainfall (~{rain_3d:.1f} mm) predicted. Save electricity and prevent waterlogging."
        elif temp > 33.0 and humidity < 50.0:
            irrigation_status = "💧 High Evapotranspiration"
            irrigation_msg = "High heat and dry air increase plant water loss. Plan light irrigation or mulching."
        else:
            irrigation_status = "🌱 Normal Irrigation"
            irrigation_msg = "Moderate conditions. Maintain standard moisture schedule based on crop stage."

        return {
            "spraying_status": spray_status,
            "spraying_msg": spray_msg,
            "irrigation_status": irrigation_status,
            "irrigation_msg": irrigation_msg
        }


weather_service = OpenMeteoWeatherService()
