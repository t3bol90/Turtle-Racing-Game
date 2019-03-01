from turtle import *
from random import randint
from random import random
import datetime
from construct.createTurtles import gencolor

<<<<<<< HEAD
def eventrand():
    Bruijn = [0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0]
    i = randint(8,31)
    X = []
    for o in range(8):
        Bitarr1 = [Bruijn[i],Bruijn[i+1],Bruijn[i+2],Bruijn[i+3],Bruijn[i+4]]
        S = Bitarr1[0]*2+Bitarr1[1]
        T = Bitarr1[2]*4 + Bitarr1[3]*2 + Bitarr1[4]*1
=======

def eventRand():
    Bruijn = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
    i = randint(0, 26)
    X = []
    for o in range(8):
        Bitarr1 = [Bruijn[i], Bruijn[i + 1], Bruijn[i + 2], Bruijn[i + 3], Bruijn[i + 4]]
        S = Bitarr1[0] * 2 + Bitarr1[1]
        T = Bitarr1[2] * 4 + Bitarr1[3] * 2 + Bitarr1[4] * 1
>>>>>>> upstream/master
        i = i - 1
        X.append(S)
        X.append(T)
    return X

<<<<<<< HEAD
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
=======
def makeTutlePos(Tur,n):
    X = []
    for i in range(n):
        temp = Tur[i].position ()
        temp = list(temp)
        X.append(temp[0])
    return X


def maktIMove(valTurtle, step):
    event = eventRand()
    min_s = 1
    max_s = 3
    currentDT = datetime.datetime.now()
    time_r = [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
    road_l = step * 20
    flag = [1, 1, 1, 1]
    tur_set = [100, 70, 40, 10]
    num_e = randint(0, road_l)
    num_f = randint(num_e, road_l)
    endPos = -150 + 20 * step
    i = randint(0,num_e)
    while(flag[0] == 1 or flag[1] == 1 or flag[2] == 1 or flag[3] == 1):
        speed = [randint(min_s, max_s), randint(min_s, max_s), randint(min_s, max_s), randint(min_s, max_s)]
        turRoadLengh = makeTutlePos(valTurtle,4)
        i = i + 1
        for j in range(4):
            if (endPos - turRoadLengh[j] >= max_s):
                if (((0 == event[2 * j + 1] or event[2 * j + 1] == 1) and (i == num_f)) or ((0 == event[4 * j + 1] or event[4 * j + 1] == 1) and (i == num_e))):
                    if (1 == event[4 * j + 1] or event[4 * j + 1] == 2):
                        e_index = event[4*j]
                    else:
                        e_index = event[2*j]
                    valTurtle[e_index].right(180)
                    valTurtle[e_index].forward(speed[e_index]*4)
                    valTurtle[e_index].right(180)
                if ((2 == event[2 * j + 1] or event[2 * j + 1] == 3) or (2 == event[4 * j + 1] or event[4 * j + 1] == 3)) and (num_e < i and i < num_f):
                    if (3 == event[4 * j + 1] or event[4 * j + 1] == 4):
                        e_index = event[4*j]
                    else:
                        e_index = event[2*j]
                    speed[e_index] = 0
                    valTurtle[e_index].color(gencolor())

                valTurtle[j].forward(speed[j])
            else:
                valTurtle[j].goto(endPos, tur_set[j])
                if (flag[j] == 1):
                    time_r[j] = datetime.datetime.now()
                    flag[j] = flag[j] - 1
>>>>>>> upstream/master
    valTurtle[0].write(currentDT.microsecond - time_r[0].microsecond)
    valTurtle[1].write(currentDT.microsecond - time_r[1].microsecond)
    valTurtle[2].write(currentDT.microsecond - time_r[2].microsecond)
    valTurtle[3].write(currentDT.microsecond - time_r[3].microsecond)
