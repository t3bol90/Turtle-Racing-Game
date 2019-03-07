from turtle import *
from random import randint


#Generate colours of turtles
def gencolor():
    r = lambda: randint(0, 255)
    return ('#%02X%02X%02X' % (r(), r(), r()))


#Create turtles absolutely
def create():
	#Set the default coordinates
	if (n == 13):
		x, y, spin = -150, 100, 0    
    tur = []

    for n in (gencolor(),gencolor(),gencolor(),gencolor()):   #Create the turtles
    #Customize the turtles
        t = Turtle()
        t.color(n)
        t.shape('turtle')

    #Move turtles to the start point
        t.penup()
        t.goto(x,y)
        t.pendown()
        y -= 30

    #Spin each turtle
        spin += 1
        if (spin % 2 == 0):
            t.right(360)
        else:
            t.left(360)

        tur.append(t)

    return tur  #Return the list of turtles
