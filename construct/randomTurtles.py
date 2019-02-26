from turtle import *
from random import randint
from random import random

def random(x, n):

    s1 = s2 = s3 = s4 = 0   #set the distance of each turtle at the startpoint

    for step in range(n * 20):

        a = randint(1,3)    #set random number of steps
        b = randint(1,3)
        c = randint(1,3)
        d = randint(1,3)

#compare and keep moving forward
        s1 += a
        if(s1 < 20 * n):
            x[0].forward(a)
        else:
            x[0].goto(-150 + 20 * n, 100)

        s2 += b
        if(s2 < 20 * n):
            x[1].forward(b)
        else:
            x[1].goto(-150 + 20 * n, 70)

        s3 += c
        if(s3 < 20 * n):
            x[2].forward(c)
        else:
            x[2].goto(-150 + 20 * n, 40)

        s4 += d
        if(s4 < 20 * n):
            x[3].forward(d)
        else:
            x[3].goto(-150 + 20 * n, 10)

#check if all turtles finish the road
        y, flag = 100, True
        for i in range(4):
            if ((x[i].pos() == (-150 + 20 * n, y)) == False):
                flag = False
                break
            else:
                y -= 30
        if (flag == True):
            break
