# 🌍 CuriousTrip

> **Il tuo compagno di viaggio definitivo direttamente da terminale!**

**CuriousTrip** è un'applicazione CLI (Command Line Interface) in Python che trasforma la pianificazione di un viaggio in un'esperienza interattiva e divertente. Inserendo il nome di un paese, l'app interroga diverse API pubbliche per generare un'elegante "Travel Card" contenente informazioni geografiche, meteo in tempo reale, tassi di cambio, consigli culinari e persino un po' di intrattenimento.

---

## ✨ Funzionalità

- 📍 **Informazioni sul Paese:** Scopri capitale, continente, popolazione, lingue ufficiali e valuta locale.
  
- 🌤️ **Meteo in Tempo Reale:** Ottieni temperatura e condizioni atmosferiche attuali della capitale.
  
- 💰 **Convertitore di Valuta:** Inserisci il tuo budget in Euro (EUR) e scopri a quanto ammonta nella valuta di destinazione.
  
- 🍽️ **Consiglio dello Chef:** Ricevi il suggerimento di un piatto tipico (o casuale) con i relativi ingredienti principali.
  
- 🐱 **Curiosità sui Gatti:** Impara qualcosa di nuovo sui nostri amici felini durante il viaggio.
  
- 😂 **Travel Joke:** Inizia il viaggio con un sorriso grazie a una barzelletta (in inglese).
  
- 💾 **Salvataggio Locale:** Esporta e salva comodamente la tua *Travel Card* in un file `.txt` per consultarla offline.

---

## 🚀 Installazione

Assicurati di avere **Python 3.x** installato sul tuo sistema.

1. **Clona il repository:**
   ```bash
   git clone [https://github.com/tuo-username/curioustrip.git](https://github.com/tuo-username/curioustrip.git)
   cd curioustrip
   ```

2. **Crea un ambiente virtuale (opzionale ma consigliato):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
   ```

3. **Installa le dipendenze:**
   Il progetto richiede la libreria `requests`.
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Utilizzo

Per avviare l'applicazione, esegui il file principale dal terminale:

```bash
python main.py
```

Segui le istruzioni a schermo:

1. Inserisci il nome del paese di destinazione (in lingua inglese, es. `Japan`, `Italy`, `Brazil`).
   
2. Inserisci il tuo budget in Euro (es. `500`).
   
3. Goditi la tua Travel Card! Alla fine, potrai scegliere se salvarla in un file di testo.
   

---

## 📂 Struttura del Progetto

Il codice è modulare e organizzato per una facile manutenzione:

```text
app/
│
├── api/
│   ├── cat_api.py       # API per le curiosità sui gatti
│   ├── country_api.py   # API per i dati geografici
│   ├── currency_api.py  # API per i tassi di cambio
│   ├── food_api.py      # API per le ricette
│   ├── joke_api.py      # API per le barzellette
│   └── weather_api.py   # API per il meteo
│
├── tools/
│   └── formatter.py     # Logica di formattazione della UI in ASCII
│
└── main.py              # Entry point dell'applicazione
```

---

## 🔌 API Utilizzate

Questo progetto non sarebbe possibile senza queste fantastiche API gratuite:

- [REST Countries](https://restcountries.com/) - Dati sui paesi
  
- [Open-Meteo](https://open-meteo.com/) - Previsioni meteo
  
- [Exchange Rate API](https://open.er-api.com/) - Tassi di cambio valute
  
- [TheMealDB](https://www.themealdb.com/) - Ricette e pasti casuali
  
- [CatFact.ninja](https://catfact.ninja/) - Curiosità sui gatti
  
- [JokeAPI](https://v2.jokeapi.dev/) - Barzellette sicure per il lavoro

---

## 📝 Licenza

Distribuito con licenza MIT. Vedi il file `LICENSE` per maggiori informazioni.
