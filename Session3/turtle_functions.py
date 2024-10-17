#turtle_functions.py
#turtle functions
import turtle

t = turtle.Turtle()

def polygon(sides, size):
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)
        
polygon(5, 100)