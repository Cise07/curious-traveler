import textwrap

def wrap_lines(text: str, width: int = 45):
    return textwrap.wrap(text, width)

def build_card(data: dict) -> str:
    box_width = 50
    lines = []

    def add_section(title):
        lines.append(f"\n{title}")

    def add_wrapped(text):
        for line in wrap_lines(text, box_width - 5):
            lines.append(f"   {line}")

    lines.append("╔" + "═" * box_width + "╗")
    lines.append("║" + "CURIOUSTRIP TRAVEL CARD".center(box_width) + "║")
    lines.append("╠" + "═" * box_width + "╣")

    add_section("📍 DESTINATION")
    lines.append(f"   Country: {data['country']}")
    lines.append(f"   Capital: {data['capital']}")
    lines.append(f"   Continent: {data['continent']}")
    lines.append(f"   Population: {data['population']:,}")
    add_wrapped(f"Languages: {data['languages']}")
    lines.append(f"   Currency: {data['currency_name']} ({data['currency_code']})")

    add_section(f"🌤️ WEATHER IN {data['capital'].upper()}")
    lines.append(f"   Temperature: {data['temperature']}°C")
    lines.append(f"   Wind: {data['wind']} km/h")
    lines.append(f"   Condition: {data['condition']}")

    add_section("💰 BUDGET")
    lines.append(
        f"   {data['budget_eur']} EUR = {data['converted_budget']:.2f} {data['currency_code']}"
    )

    add_section("🍽️ CHEF'S RECOMMENDATION")
    add_wrapped(f"Dish: {data['meal_name']}")
    lines.append(f"   Category: {data['meal_category']}")
    add_wrapped(f"Ingredients: {data['meal_ingredients']}")

    add_section("🐱 CAT TRIVIA")
    add_wrapped(f"\"{data['cat_fact']}\"")

    add_section("😂 TRAVEL JOKE (English)")
    add_wrapped(f"\"{data['joke']}\"")

    lines.append("╚" + "═" * box_width + "╝")

    return "\n".join(lines)
