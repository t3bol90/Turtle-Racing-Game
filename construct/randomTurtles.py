from turtle import *
from random import randint
from random import random

def random(x, n):

    s = s1 = s2 = s3 = 0
    for step in range(300):
        a = randint(1,3)
        b = randint(1,3)
        c = randint(1,3)
        d = randint(1,3)
        if(s < 20*n):
            s += a
            x[0].forward(a)
        else:
            x[0].goto(-150 + s, 100)

        if(s1 < 20*n):
            s1 += b
            x[1].forward(b)
        else:
            x[1].goto(-150 + s, 70)

        if(s2 < 20*n):
            s2 += c
            x[2].forward(c)
        else:
            x[2].goto(-150 + s, 40)

        if(s3 < 20*n):
            s3 += d
            x[3].forward(d)
        else:
            x[3].goto(-150 + s, 10)
