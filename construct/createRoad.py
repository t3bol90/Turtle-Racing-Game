from turtle import *

#Create short road
def create():
    speed(0)
    penup()
    goto(-140,140)  #Set the default position
    n = 0
    bgcolor("white")

    screensize(480, 360)

    n = int(textinput("Turtles' race","Please input the length of the road"))
    n = n + 1
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
    return n
