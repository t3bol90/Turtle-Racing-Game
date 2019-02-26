from turtle import *
from random import randint
from random import random
from typing import Any, Union
import datetime


def eventrand():
    Bruijn = [0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0]
    i = randint(4,31)
    X = []
    for o in range(4):
        Bitarr1 = [Bruijn[i],Bruijn[i+1],Bruijn[i+2],Bruijn[i+3],Bruijn[i+4]]
        S = Bitarr1[0]*2+Bitarr1[1]
        T = Bitarr1[2]*4 + Bitarr1[3]*2 + Bitarr1[4]*1
        T = T%4
        i = i - 1
        X.append(S)
        X.append(T)
    return X

def random(x, n):
    Event = eventrand()
    s1 = s2 = s3 = s4 = 0
    E = [1,1,1,1]
    for i in range(4):
        E[Event[2*i]] = int(Event[2*i+1])
    num_e = randint(0,n)
    num_f = randint(0,n)
    currentDT = datetime.datetime.now()
    for step in range(n*20):
        a = randint(1,3)
        b = randint(1,3)
        c = randint(1,3)
        d = randint(1,3)
        if(s1 < 20 * n):
            if (E[0] == 0 and step == num_e):
                a = 0
                x[0].write("Stuning",font=("Arial", 5, "normal"))
            if (E[0] == 2 and step == num_f):
                x[0].right(180)
                x[0].forward(a*3)
                x[0].right(180)
                s1-=3*a
            s1 += a
            x[0].forward(a)
        else:
            x[0].goto(-150 + 20 * n, 100)
            S1DT = datetime.datetime.now()
        if(s2 < 20 * n):
            if (E[1] == 0 and step == num_e):
                b = 0
                x[1].write("Stuning",font=("Arial", 5, "normal"))
            if (E[1] == 2 and step == num_f):
                x[1].right(180)
                x[1].forward(b * 3)
                x[1].right(180)
                s2-=3 * b
            s2 += b
            x[1].forward(b)
        else:
            x[1].goto(-150 + 20 * n, 70)
            S2DT = datetime.datetime.now()
        if(s3 < 20 * n):
            if (E[2] == 0 and step == num_e):
                c = 0
                x[2].write("Stuning",font=("Arial", 5, "normal"))
            if (E[2] == 2 and step == num_f):
                x[2].right(180)
                x[2].forward(c * 3)
                x[2].right(180)
                s3-=3 * c
            s3 += c
            x[2].forward(c)

        else:
            x[2].goto(-150 + 20 * n, 40)
            S3DT = datetime.datetime.now()
        if(s4 < 20 * n):
            if E[3] == 0 and step == num_e:
                d = 0
                x[3].write("Stuning",font=("Arial", 5, "normal"))
            if E[3] == 2 and step == num_f:
                x[3].right(180)
                x[3].forward(d * 3)
                x[3].right(180)
                s4-=3 * d
            s4 += d
            x[3].forward(d)
        else:
            x[3].goto(-150 + 20 * n, 10)
            S4DT = datetime.datetime.now()
    x[0].write(currentDT.microsecond - S1DT.microsecond)
    x[1].write(currentDT.microsecond - S2DT.microsecond)
    x[2].write(currentDT.microsecond - S3DT.microsecond)
    x[3].write(currentDT.microsecond - S4DT.microsecond)

