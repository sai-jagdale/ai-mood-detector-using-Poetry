# using SpeechRecognition for voice input and TextBlob for sentiment analysis.
# A simple AI that detects if the user is happy or sad based on text or voice input.

import speech_recognition as sr
from textblob import TextBlob

class EmotionAI:
    def __init__(self):
        # Initialize the "Ears" (Recognizer)
        self.recognizer = sr.Recognizer()
        print("--- 🤖 AI System Initialized ---")

    def get_voice_input(self):
        """Listens to the microphone and uses Google API to convert to text."""
        print("\n🎤 Listening... (Please speak now)")
        
        with sr.Microphone() as source:
            # Adjust for background noise automatically
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("⏳ Sending audio ...")
            # This uses the Google Speech Recognition API 
            # Not using any personl API key here , just using the free API key.
            # For learning, we use the default free key.
            text = self.recognizer.recognize_google(audio)
            print(f"📝 Heard: '{text}'")
            return text
        except sr.UnknownValueError:
            print("❌ Google could not understand the audio.")
            return None
        except sr.RequestError:
            print("❌ Could not request results from Google API (Check internet).")
            return None

    def predict_emotion(self, text):
        """The ML 'Brain' that decides if the text is Happy or Sad."""
        if not text:
            return "Unknown"

        analysis = TextBlob(text)
        score = analysis.sentiment.polarity  # -1 to +1

        # Our custom "Emotion logic"
        if score > 0.5:
            return "🥰 Ecstatic / Very Happy"
        elif score > 0:
            return "🙂 Happy / Positive"
        elif score == 0:
            return "😐 Neutral"
        elif score > -0.5:
            return "🙁 Sad / Negative"
        else:
            return "😡 Furious / Very Negative"

    def run(self):
        print("Choose Input Mode:")
        print("1. Type Text")
        print("2. Use Voice (Microphone)")
        
        choice = input("Enter 1 or 2: ")

        user_input = ""

        if choice == '1':
            user_input = input("Type your sentence: ")
        elif choice == '2':
            user_input = self.get_voice_input()
        else:
            print("Invalid choice!")
            return

        # Perform Prediction
        if user_input:
            emotion = self.predict_emotion(user_input)
            print("\n" + "="*30)
            print(f"🗣️  Input:  {user_input}")
            print(f"🔮  Prediction: {emotion}")
            print("="*30)

if __name__ == "__main__":
    bot = EmotionAI()
    bot.run()