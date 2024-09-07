from flask import Flask, render_template, request
import random
import threading
import pyautogui
import time

app = Flask(__name__)

messages = [
    "strange.exe",
    "Hellooo!",
    "Hello from strange!",
    "<:yummi:1176178649842589758>",
]

def generate_random_message():
    return random.choice(messages)

class Spammer:
    def __init__(self):
        self.running = False
        self.spammer_thread = None

    def start_spamming(self):
        if not self.running:
            self.running = True
            self.spammer_thread = threading.Thread(target=self.spamming_loop)
            self.spammer_thread.start()

    def spamming_loop(self):
        while self.running:
            pyautogui.typewrite("oh")
            pyautogui.press("enter")
            time.sleep(5)
            pyautogui.typewrite(generate_random_message())
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.typewrite("+:yummi:")
            pyautogui.press("enter")
            time.sleep(5)
            pyautogui.typewrite("ob")
            pyautogui.press("enter")
            time.sleep(5)

    def stop_spamming(self):
        self.running = False
        self.spammer_thread.join()

spammer = Spammer()

@app.route("/")
def index():
    return render_template("index.html", button_text="Start Spamming")

@app.route("/toggle_spamming", methods=["POST"])
def toggle_spamming_route():
    if spammer.running:
        spammer.stop_spamming()
        return "Spamming stopped."
    else:
        spammer.start_spamming()
        return "Spamming started."

if __name__ == "__main__":
    app.run(debug=True)