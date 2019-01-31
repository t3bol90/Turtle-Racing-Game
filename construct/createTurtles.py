from turtle import *

def create():
    x, y, spin = -160, 100, 0    #set the default coordinates
    tur = []

    for n in ('#3FAABF','#C14242','#41BF3F','#A13FBF'):   #create the turtles
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
