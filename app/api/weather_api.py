import requests

def get_weather(lat: float, lon: float) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )
    res = requests.get(url).json()
    weather = res.get("current_weather", {})

    condition = "☀️ Clear sky" if weather.get("weathercode") == 0 else "☁️ Cloudy/Variable"

    return {
        "temperature": weather.get("temperature"),
        "wind": weather.get("windspeed"),
        "condition": condition,
    }
