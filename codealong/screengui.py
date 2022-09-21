from ast import While
from http.client import CONTINUE
import turtle
import random
import math
import time

poop = turtle.Screen()
peepoo = turtle.Turtle()

poop.colormode(255)
while True:
    peepoo.penup()
    peepoo.goto(random.randint(1,30),random.randint(1,30))
    peepoo.pendown()
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    peepoo.color((r,g,b))
    cat = 0
    sides = int(poop.numinput("sides","How many sides do you want? "))
    angle = 360 / sides
    distance = 360/(sides/2)
    peepoo.begin_fill()

    #background color
    colorquestion = poop.textinput("Background","Do you want a random color background or specific?")
    if colorquestion == "SPECIFIC".lower():
        colorinput = poop.textinput("Color","What color do you want?")
    else:
        colorinput = "#" + str(random.randint(10000,99999))

    poop.bgcolor(colorinput)

    while cat < sides:
        peepoo.forward(distance)
        peepoo.right(angle)
        cat += 1

    #end
    answer = poop.textinput("Dialogue", "Do you want to quit or retry? Type 'Quit' or 'Retry'")
    if answer == "QUIT".lower():
        exit()
    elif answer == "RETRY".lower():
        continue
    else:
        exit()
