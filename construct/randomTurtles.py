from turtle import *
from random import randint
from random import random
from typing import Any, Union
import datetime

def eventrand():
    Bruijn = [0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0]
    i = randint(8,31)
    X = []
    for o in range(8):
        Bitarr1 = [Bruijn[i],Bruijn[i+1],Bruijn[i+2],Bruijn[i+3],Bruijn[i+4]]
        S = Bitarr1[0]*2+Bitarr1[1]
        T = Bitarr1[2]*4 + Bitarr1[3]*2 + Bitarr1[4]*1
        i = i - 1
        X.append(S)
        X.append(T)
    return X

def random(valTurtle, step):
    event = eventrand()
    min_s = 1
    max_s = 3
    turRoadLengh = [0,0,0,0]
    currentDT = datetime.datetime.now()
    time_r = [datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now()]
    road_l = step*12
    flag = [1,1,1,1]
    tur_set = [100,70,40,10]
    num_e = randint(1, road_l)
    num_f = randint(1, road_l)
    for i in range(road_l):
        speed = [randint(min_s,max_s),randint(min_s,max_s),randint(min_s,max_s),randint(min_s,max_s)]
        road_l -= min(speed)
        for j in range(4):
            if (turRoadLengh[j] < 20 * step and flag[j] >= 1):
                if ((1 == event[2*j + 1] or event[2*j + 1] == 2)and(i == num_e))or((1 == event[4*j + 1] or event[4*j + 1] == 2)and(i == num_f)):
                    valTurtle[event[2*j]].right(180)
                    valTurtle[event[2*j]].forward(speed[event[2*j]]*4)
                    valTurtle[event[2*j]].right(180)
                    turRoadLengh[event[2*j]] -= speed[event[2*j]]
                if((3 == event[2*j+1] or event[2*j +1] == 4)) and (i == num_e) or((3 == event[4*j + 1] or event[4*j+1] == 4) and (i==num_f)):
                    speed[event[2*j]] = 0
                    valTurtle[event[2*j]].write("Stuning", font=("Arial", 5, "normal"))
                turRoadLengh[j] += speed[j]
                valTurtle[j].forward(speed[j])
            else:
                flag[j] = flag[j] - 1
                valTurtle[j].goto(-150 + 20 * step, tur_set[j])
                time_r[j] = datetime.datetime.now()
    valTurtle[0].write(currentDT.microsecond - time_r[0].microsecond)
    valTurtle[1].write(currentDT.microsecond - time_r[1].microsecond)
    valTurtle[2].write(currentDT.microsecond - time_r[2].microsecond)
    valTurtle[3].write(currentDT.microsecond - time_r[3].microsecond)
