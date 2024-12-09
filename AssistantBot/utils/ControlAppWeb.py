import os
import webbrowser
import pyautogui
import time
class ControlAppWeb:
    """Control apps and web browsers."""

    def __init__(self, assistant):
        self.assistant = assistant
        self.dict_app = {
            "command prompt": "cmd",
            "paint": "mspaint",
            "word": "winword",
            "excel": "excel",
            "chrome": "chrome",
            "vscode": "code",
            "powerpoint": "powerpnt",
        }

    def open_webapp(self, command):
        """Open a website or application."""
        self.assistant.speak("Opening, sir.")
        if ".com" in command or ".org" in command:
            webbrowser.open(f"https://www.{command.replace('open', '').strip()}")
        else:
            for app, process in self.dict_app.items():
                if app in command:
                    os.system(f"start {process}")

    def close_app_web(self, command):
        """Close tabs or applications."""
        if "tab" in command:
            count = int(command.split(" ")[0]) if command.split(" ")[0].isdigit() else 1
            for _ in range(count):
                pyautogui.hotkey("ctrl", "w")
                time.sleep(0.2)
            self.assistant.speak(f"Closed {count} tab(s).")
        else:
            for app, process in self.dict_app.items():
                if app in command:
                    os.system(f"taskkill /f /im {process}.exe")

    def open_new_tab(self):
        """Open a new browser tab."""
        self.assistant.speak("Opening a new tab, sir.")
        pyautogui.hotkey("ctrl", "t")

    def navigate_tabs(self, direction="next"):
        """Navigate to the next or previous tab."""
        if direction == "next":
            self.assistant.speak("Navigating to the next tab, sir.")
            pyautogui.hotkey("ctrl", "tab")
        elif direction == "previous":
            self.assistant.speak("Navigating to the previous tab, sir.")
            pyautogui.hotkey("ctrl", "shift", "tab")
        else:
            self.assistant.speak("Invalid command. Please say 'next' or 'previous', sir.")