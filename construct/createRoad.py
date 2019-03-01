from turtle import *
from construct.createTurtles import gencolor
def makeshort(n):
    n = int(10)
def makelong(n):
    n = int(20)
def makemedium(n):
    n = int(15)
    
def create():
    speed(0)
    penup()     #set the default position
    goto(-140,140)
    n = 0
    bgcolor("white")
    # onkey(makeshort(n),"U")
    # onkey(makelong(n),"O")
    # onkey(makemedium(n),"I")
    # listen()

    screensize(480, 360)

    n = int(textinput("Noti from Pornhub ", "Please enter the length of the road:  "))
    n = n + 1
    for step in range(n):   #draw lines of the road
        write(step, align = 'center')
        right(90)
        forward(10)
        for step in range (15): #draw dashed lines
            forward(10)
            if (step % 2 == 0): penup()
            else: pendown()

        penup() #return and start drawing the next line
        backward(160)
        left(90)
        forward(20)
    return n
