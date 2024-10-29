#turtle_functions.py
#turtle functions
from turtle import Turtle

t = Turtle()

    
def polygon(sides, size):
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)
        
polygon(6, 100)