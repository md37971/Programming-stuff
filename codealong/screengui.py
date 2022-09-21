from ast import While
import turtle
import random
import math
import time

poop = turtle.Screen()
peepoo = turtle.Turtle()

poop.colormode(255)
while True:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    peepoo.color((r,g,b))

    cat = 0
    sides = int(poop.numinput("sides","How many sides do you want? "))
    angle = 360 / sides
    distance = 360/(sides/2)
    peepoo.begin_fill()

    while cat < sides:
        peepoo.forward(distance)
        peepoo.right(angle)
        cat += 1

turtle.Screen().exitonclick()