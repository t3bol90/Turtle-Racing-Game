from turtle import *

def create():
    speed(0)
    penup()     #set the default position
    goto(-140,140)

    n = int(input("Please enter the length of the road: "))

    for step in range(n):   #draw lines of the road
        write(step, align = 'center')
        right(90)
        forward(10)
        pendown()

        for step in range (15): #draw dashed lines
            forward(10)
            if (step % 2 == 0): penup()
            else: pendown()

        penup() #return and start drawing the next line
        backward(160)
        left(90)
        forward(20)
    return n
