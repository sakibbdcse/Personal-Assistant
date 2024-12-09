import pyttsx3
import speech_recognition as sr
class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.current_voice = "female"  # Default voice set to female
        self.set_voice(voice_gender=self.current_voice)  # Set the default voice to female
        self.set_rate(170)

    def set_voice(self, voice_gender="male"):
        """Set Assistant Voice male or female"""
        if voice_gender.lower() == "male":
            self.engine.setProperty("voice", self.voices[0].id)
            self.current_voice = "male"
        elif voice_gender.lower() == "female":
            if len(self.voices) > 1:
                self.engine.setProperty("voice", self.voices[1].id)
                self.current_voice = "female"
            else:
                print("Female voice not available. Using default male voice.")
        else:
            print("Invalid gender. Please choose 'male' or 'female'.")

    def toggle_voice(self):
        """Toggle the voice between male and female"""
        if self.current_voice == "male":
            self.set_voice("female")
            self.speak("Voice changed to female.")
        else:
            self.set_voice("male")
            self.speak("Voice changed to male.")

    def set_rate(self, rate=170):
        """Set the rate of speech."""
        self.engine.setProperty("rate", rate)

    def speak(self, audio):
        """Convert text to speech."""
        self.engine.say(audio)
        self.engine.runAndWait()

    def take_command(self):
        """Capture and process user voice input."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            recognizer.energy_threshold = 300
            try:
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
                print("Processing...")
                query = recognizer.recognize_google(audio, language='en-bn')
                print(f"You said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                print("Could not understand your voice. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            return "None"