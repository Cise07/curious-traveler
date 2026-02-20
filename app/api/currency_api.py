import requests

def convert_eur_to(currency_code: str, amount_eur: float) -> float:
    res = requests.get("https://open.er-api.com/v6/latest/EUR").json()
    rate = res.get("rates", {}).get(currency_code, 1)
    return amount_eur * rate
