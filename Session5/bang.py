#  bang.py
import time

last_time = time.monotonic()
interval = 2.0
message = "Bang!"
last_time2 = time.monotonic()
interval2 = 1.0
message2 = "Boom!"

while True:
    now = time.monotonic()
    if now - last_time > interval:
        print(message)
        last_time = now
    if now - last_time2 > interval2:
        print(message2)
        last_time2 = now