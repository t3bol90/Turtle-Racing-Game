from turtle import *
from construct.createTurtles import gencolor


#Create road of course
def create(n):
    speed(0)
    penup()
    goto(-140,140)  #Set the default position
    bgcolor("white")

    screensize(480, 360)

    #Draw lines of the road
    for step in range(n):
        write(step, align = 'center')
        right(90)
        #Draw dashed lines
        for step in range (15):
            forward(10)
            if (step % 2 == 0): penup()
            else: pendown()
        #Start drawing the next line
        penup()
        backward(150)
        left(90)
        forward(20)
