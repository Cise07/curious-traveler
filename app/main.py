import time

from api.country_api import get_country_info
from api.weather_api import get_weather
from api.currency_api import convert_eur_to
from api.food_api import get_random_meal
from api.cat_api import get_cat_fact
from api.joke_api import get_joke

from tools.formatter import build_card


def loading(message: str):
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print(" ✅")


def curious_trip():
    print("\n=== CURIOUSTRIP ===\n")

    country_input = input("🌍 Enter the destination country (in English):").strip()
    if not country_input:
        print("❌ Country name cannot be empty.")
        return

    try:
        loading("🔎 Fetching country info")
        country = get_country_info(country_input)

        loading("🌤️ Fetching weather")
        weather = get_weather(country["lat"], country["lon"])

        budget_eur = float(input(f"💰 Enter your budget in EUR for {country['name']}: "))

        loading("💱 Converting currency")
        converted = convert_eur_to(country["currency_code"], budget_eur)

        loading("🍽️ Fetching food recommendation")
        meal = get_random_meal()

        loading("🐱 Fetching cat fact")
        cat_fact = get_cat_fact()

        loading("😂 Fetching travel joke")
        joke = get_joke()

        loading("🧾 Building your travel card")

        card_data = {
            "country": country["name"],
            "capital": country["capital"],
            "continent": country["continent"],
            "population": country["population"],
            "languages": country["languages"],
            "currency_name": country["currency_name"],
            "currency_code": country["currency_code"],
            "temperature": weather["temperature"],
            "wind": weather["wind"],
            "condition": weather["condition"],
            "budget_eur": budget_eur,
            "converted_budget": converted,
            "meal_name": meal["name"],
            "meal_category": meal["category"],
            "meal_ingredients": meal["ingredients"],
            "cat_fact": cat_fact,
            "joke": joke,
        }

        card = build_card(card_data)
        print("\n" + card)

        try:

            filename = f"trip_card_{country['name'].replace(' ', '_')}.txt"
        
        # Chiedi conferma all'utente
            scelta = input(f"\n❓ Do you want to save the card for {country['name']}? (Y/N): ").strip().lower()

            if scelta=='y':
                with open(filename, "w", encoding="utf-8") as f:
                 f.write(card)
                print(f"💾 Saved as: {filename}")
            else:
                print("❌ save cancelled by the user.")

        except Exception as e:
            print(f"❌ Error: {e}")
            
    except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    curious_trip()
