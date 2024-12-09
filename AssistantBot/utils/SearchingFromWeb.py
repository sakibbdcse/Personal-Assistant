import pywhatkit
import wikipedia
class SearchingFromWeb:
    def __init__(self, assistant):
        self.assistant = assistant

    def search_google(self, command):
        """Search Google or Wikipedia based on the user's command."""
        if "google" in command:
            self.assistant.speak("Searching on Google...")
            command = command.replace("google", "").strip()
            try:
                pywhatkit.search(command)
                result = wikipedia.summary(command, sentences=1)
                self.assistant.speak(result)
            except Exception:
                self.assistant.speak("I couldn't find any relevant results.")

    def search_youtube(self, command):
        """Search YouTube based on the user's command."""
        if "youtube" in command:
            self.assistant.speak("Searching on YouTube...")
            command = command.replace("youtube", "").strip()
            pywhatkit.playonyt(command)
            self.assistant.speak("Playing your selection.")

    def search_wikipedia(self, command):
        """Search Wikipedia based on the user's command."""
        if "wikipedia" in command:
            self.assistant.speak("Searching on Wikipedia...")
            command = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(command, sentences=2)
                self.assistant.speak(f"According to Wikipedia: {result}")
            except wikipedia.exceptions.DisambiguationError:
                self.assistant.speak("There are multiple results for your query.")
            except wikipedia.exceptions.PageError:
                self.assistant.speak("I couldn't find any results.")
            except Exception as e:
                self.assistant.speak(f"An error occurred: {e}")