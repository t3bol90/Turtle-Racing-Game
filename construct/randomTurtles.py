from turtle import *
from random import randint
from random import random

def random(x):
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
