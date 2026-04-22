import requests
from config import WEATHER_API_KEY, CITY, COUNTRY_CODE


def get_weather_data():
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={CITY},{COUNTRY_CODE}&appid={WEATHER_API_KEY}&units=metric&lang=de"
        )

        response = requests.get(url, timeout=5)
        data = response.json()

        return {
            "temperature": round(data["main"]["temp"]),
            "description": data["weather"][0]["description"].capitalize(),
            "location": data["name"]
        }

    except Exception:
        return {
            "temperature": "--",
            "description": "Wetterdaten nicht verfügbar",
            "location": CITY
        }