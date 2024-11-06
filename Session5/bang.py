#  bang.py
import time

message = "Bang!"
last_time = time.monotonic()
interval = 2.0

while True:
    now = time.monotonic()
    if now - last_time > interval:
        print(message)
        last_time = now