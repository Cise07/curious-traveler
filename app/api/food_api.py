import requests

def get_random_meal() -> dict:
    meal = requests.get(
        "https://www.themealdb.com/api/json/v1/1/random.php"
    ).json()["meals"][0]

    ingredients = [
        meal[f"strIngredient{i}"]
        for i in range(1, 6)
        if meal.get(f"strIngredient{i}")
    ]

    return {
        "name": meal["strMeal"],
        "category": meal["strCategory"],
        "ingredients": ", ".join(ingredients),
    }
