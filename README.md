# 🌍 CuriousTrip

> **Your ultimate travel companion directly from the terminal!**

**CuriousTrip** is a Python CLI (Command Line Interface) application that transforms travel planning into an interactive and fun experience. By entering the name of a country, the app queries several public APIs to generate an elegant "Travel Card" containing geographical information, real-time weather, exchange rates, culinary tips, and even a bit of entertainment.

---

## ✨ Features

- 📍 **Country Information:** Discover capital, continent, population, official languages, and local currency.
  
- 🌤️ **Real-Time Weather:** Get current temperature and atmospheric conditions for the capital city.
  
- 💰 **Currency Converter:** Enter your budget in Euro (EUR) and find out how much it amounts to in the destination currency.
  
- 🍽️ **Chef's Recommendation:** Receive a suggestion for a typical (or random) dish with its main ingredients.
  
- 🐱 **Cat Facts:** Learn something new about our feline friends during your trip.
  
- 😂 **Travel Joke:** Start your journey with a smile thanks to a joke (in English).
  
- 💾 **Local Saving:** Conveniently export and save your *Travel Card* to a `.txt` file for offline consultation.

---

## 🎥 Program Demo 

![Demo](https://github.com/user-attachments/assets/64971928-9d55-42f2-8e89-baabd68209e0)

---

## 🚀 Installation

Make sure you have **Python 3.x** installed on your system.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Cise07/curious-traveler curious-traveler
   cd curious-traveler
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv

   # On Mac use:
   source venv/bin/activate
   
   # On Windows use:
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   The project requires the `requests` library.
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Usage

To start the application, run the main file from the terminal:

```bash
# Move into the 'app' directory
cd app

# Run the 'main.py' file
python main.py
```

Follow the on-screen instructions:

1. Enter the name of the destination country (in English, e.g., `Japan`, `Italy`, `Brazil`).
   
2. Enter your budget in Euro (e.g., `500`).
   
3. Enjoy your Travel Card! At the end, you can choose whether to save it to a text file.
   

---

## 📂 Project Structure

The code is modular and organized for easy maintenance:

```text
app/
│
├── api/
│   ├── cat_api.py       # API for cat facts
│   ├── country_api.py   # API for geographical data
│   ├── currency_api.py  # API for exchange rates
│   ├── food_api.py      # API for recipes
│   ├── joke_api.py      # API for jokes
│   └── weather_api.py   # API for weather
│
├── tools/
│   └── formatter.py     # UI formatting logic in ASCII
│
└── main.py              # Application entry point
```

---

## 🔌 APIs Used

This project wouldn't be possible without these fantastic free APIs:

- [REST Countries](https://restcountries.com/) - Country data
  
- [Open-Meteo](https://open-meteo.com/) - Weather forecasts
  
- [Exchange Rate API](https://open.er-api.com/) - Currency exchange rates
  
- [TheMealDB](https://www.themealdb.com/) - Recipes and random meals
  
- [CatFact.ninja](https://catfact.ninja/) - Cat facts
  
- [JokeAPI](https://v2.jokeapi.dev/) - Safe-for-work jokes

---

## 📝 License

Distributed under the MIT License. See the `LICENSE` file for more information.
