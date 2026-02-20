import requests

def get_joke() -> str:
    j = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode").json()

    if j.get("type") == "single":
        return j.get("joke")
    return f"{j.get('setup')} ... {j.get('delivery')}"
