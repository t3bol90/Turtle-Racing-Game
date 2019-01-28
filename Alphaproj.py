from turtle import*
from random import randint
from random import random
speed(0)
penup()
goto(-140,140)
n = int(input())
for step in range(n):
    write(step)
    right(90)
    forward(10)
    pendown()
    for step in range (15):
        forward(10)
        if step%2==0: penup()
        else: pendown()
    penup()
    backward(160)
    left(90)
    forward(20)

red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160,100)
red.pendown()

blue = Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160,70)
blue.pendown()

green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160,40)
green.pendown()

orange = Turtle()
orange.color('orange')
orange.shape('turtle')
orange.penup()
orange.goto(-160,10)
orange.pendown()

for turn in range(1):
    red.right(360)
    blue.left(360)
    green.right(360)
    orange.left(360)

s = s1 = s2 = s3 = 0
for step in range(300):
    a = randint(1,3)
    b = randint(1,3)
    c = randint(1,3)
    d = randint(1,3)
    if(s < 20*n):  
        s = s + a
        red.forward(a)
    else:
        red.goto(-150 + s, 100)

    if(s1 < 20*n):  
        s1 = s1 + b
        blue.forward(b)
    else:
        blue.goto(-150 + s, 70)

    if(s2 < 20*n):  
        s2 = s2 + c
        green.forward(c)
    else:
        green.goto(-150 + s, 40)

    if(s3 < 20*n): 
        s3 = s3 + d
        orange.forward(d)
    else:
        orange.goto(-150 + s, 10)