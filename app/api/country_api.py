import requests

def get_country_info(country_name: str) -> dict:
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    res = requests.get(url)

    if res.status_code != 200:
        raise ValueError("Country not found")

    data = res.json()[0]

    return {
        "name": data.get("name", {}).get("common"),
        "capital": data.get("capital", ["N/A"])[0],
        "population": data.get("population"),
        "continent": data.get("continents", ["N/A"])[0],
        "languages": ", ".join(data.get("languages", {}).values()),
        "currency_code": list(data.get("currencies", {}).keys())[0],
        "currency_name": data["currencies"][list(data["currencies"].keys())[0]]["name"],
        "lat": data.get("capitalInfo", {}).get("latlng", [0, 0])[0],
        "lon": data.get("capitalInfo", {}).get("latlng", [0, 0])[1],
    }
