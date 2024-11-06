# my_timer.py
import time

class Timer:
    def __init__(self, message, interval):
        self.message = message
        self.interval = interval
        self.last_time = time.monotonic()
        
    def update(self):
        now = time.monotonic()
        if now - self.last_time > self.interval:
            print(self.message)
            self.last_time = now