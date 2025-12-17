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

## 📦 Installation

### 1. Setup Project
Clone the repository or open the project folder in VS Code.

### 2. Install Dependencies
Run the following command to automatically install all required libraries (TextBlob, PyAudio, etc.):

```bash
poetry install

## ⚠️ Windows Audio Setup (Important)
If you are on Windows and the microphone doesn't work, or you see PyAudio installation errors, run these commands to fix the binary dependencies:

```bash
poetry run pip install pipwin
poetry run pipwin install pyaudio

## 🎮 How to Run
To start the application, use Poetry to execute the main script:

```bash
poetry run python main.py

Once running, follow the on-screen menu:

Plaintext
Choose Input Mode:
1. Type Text
2. Use Voice (Microphone)
Enter 1 or 2: 
📝 Example Usage
Select 1: Text Input
Input: "I am really frustrated with this people."

Result: 😡 Furious / Very Negative

Select 2: Voice Input
Input: (Speak into microphone) "I am so happy today!"

Result: 🥰 Ecstatic / Very Happy