# my_oop.py
import my_timer

timer1 = my_timer.Timer("Bang!", 2.0)
timer2 = my_timer.Timer("Boom!", 1.0)
timer3 = my_timer.Timer("Wham!", 3.0)

while True:
    timer1.update()
    timer2.update()
    timer3.update()