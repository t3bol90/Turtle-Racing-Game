from turtle import *
from construct.createTurtles import gencolor

#Creat buttons of road's length
def makeshort(n):
    n = int(10)
def makelong(n):
    n = int(20)
def makemedium(n):
    n = int(15)

#Create Road
def create():
    speed(0)
    penup()
    goto(-140,140)   #Set the default position
    n = 0
    bgcolor("white")
    # onkey(makeshort(n),"U")
    # onkey(makelong(n),"O")
    # onkey(makemedium(n),"I")
    # listen()

    screensize(480, 360)

    n = int(textinput("Noti from Pornhub ", "Please enter the length of the road:  "))
    n = n + 1
    #Draw lines of the road
    for step in range(n):
        write(step, align = 'center')
        right(90)
        forward(10)
        #Draw dashed lines
        for step in range (1,16):
            forward(10)
            if (step % 2 == 0): penup()
            else: pendown()
        #Return and start drawing the next line
        penup()
        backward(160)
        left(90)
        forward(20)
    return n
