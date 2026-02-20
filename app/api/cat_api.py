import requests

def get_cat_fact() -> str:
    return requests.get("https://catfact.ninja/fact").json().get("fact")
