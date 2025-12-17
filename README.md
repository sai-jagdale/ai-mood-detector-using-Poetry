# 🎭 AI Mood Detector (Text & Voice)

A simple, multimodal AI application that detects human emotions using **Natural Language Processing (NLP)**. This project allows users to either **type text** or **speak** via their microphone, using Google's Speech Recognition to transcribe audio and TextBlob to analyze sentiment.

## 🚀 Features

* **🗣️ Dual Input System:**
    * **Text Mode:** Type any sentence directly to get an instant emotion analysis.
    * **Voice Mode:** Speak naturally into your microphone. The app listens, converts your speech to text, and then analyzes it.
* **🧠 Sentiment Analysis:** Uses **TextBlob** to calculate a polarity score (-1 to +1) and classifies emotions into categories like "Ecstatic", "Happy", "Neutral", "Sad", or "Furious".
* **🎙️ Automatic Speech Recognition:** Integrated with **Google Speech Recognition** (using the default free API key) for easy testing without complex setup.
* **📦 Poetry Managed:** Built with a clean, reproducible dependency environment.

## 🛠️ Technologies Used

* **Language:** Python 3.13+
* **Dependency Manager:** Poetry
* **Voice Processing:** `SpeechRecognition`, `PyAudio`
* **NLP Engine:** `TextBlob`, `NLTK`
* **Data Handling:** `Pandas` (Included in dependencies)

## 📂 Project Structure

```text
AI-MOOD-DETECTOR/
├── .venv/                   # Virtual Environment (where libraries like TextBlob live)
├── src/
│   └── ai_mood_detector/    # Source package folder
│       └── __init__.py
├── tests/                   # Test suite folder
│   └── __init__.py
├── main.py                  # The main application script
├── poetry.lock              # Locks exact library versions
├── pyproject.toml           # Project configuration & dependencies
└── README.md                # This documentation
