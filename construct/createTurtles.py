from turtle import *
from random import randint
def create():
    x, y, spin = -150, 100, 0    #set the default coordinates
    tur = []

    for n in (gencolor(),gencolor(),gencolor(),gencolor()):   #create the turtles
    #customize the turtles
        t = Turtle()
        t.color(n)
        t.shape('turtle')

    #move turtles to the start point
        t.penup()
        t.goto(x,y)
        t.pendown()
        y -= 30

    #spin each turtle
        spin += 1
        if (spin % 2 == 0):
            t.right(360)
        else:
            t.left(360)

        tur.append(t)

    return tur  #return the list of turtles
def gencolor():
    r = lambda: randint(0, 255)
    return ('#%02X%02X%02X' % (r(), r(), r()))

