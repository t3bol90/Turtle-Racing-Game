from turtle import *
from random import randint
from random import random

def random(x, n):

    s1 = s2 = s3 = s4 = 0
    for step in range(n * 20):
        a = randint(1,3)
        b = randint(1,3)
        c = randint(1,3)
        d = randint(1,3)
        if(s1 < 20 * n):
            s1 += a
            x[0].forward(a)
        else:
            x[0].goto(-150 + 20 * n, 100)

        if(s2 < 20 * n):
            s2 += b
            x[1].forward(b)
        else:
            x[1].goto(-150 + 20 * n, 70)

        if(s3 < 20 * n):
            s3 += c
            x[2].forward(c)
        else:
            x[2].goto(-150 + 20 * n, 40)

        if(s4 < 20 * n):
            s4 += d
            x[3].forward(d)
        else:
            x[3].goto(-150 + 20 * n, 10)
