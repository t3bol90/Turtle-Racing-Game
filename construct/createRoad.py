from turtle import *

#Create short road
def createShort():
    speed(0)
    penup()
    goto(-140,140)  #Set the default position
    n = 0
    bgcolor("white")

    screensize(480, 360)

    n = 11
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

#Create medium road
def createMedium():
    speed(0)
    penup()
    goto(-140,140)  #Set the default position
    n = 0
    bgcolor("white")

    screensize(480, 360)

    n = 16
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

#Create long road
def createLong():
    speed(0)
    penup()
    goto(-140,140)  #Set the default position
    n = 0
    bgcolor("white")

    screensize(480, 360)

    n = 21
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
