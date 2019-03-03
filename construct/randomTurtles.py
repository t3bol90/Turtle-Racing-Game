from turtle import *
from random import randint, shuffle
from random import random
from construct.createTurtles import gencolor
from time import perf_counter


def eventRand():
    Bruijn = [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]
    i = randint (0, 26)
    X = []
    for o in range (8):
        Bitarr1 = [Bruijn[i], Bruijn[i + 1], Bruijn[i + 2], Bruijn[i + 3], Bruijn[i + 4]]
        S = Bitarr1[0] * 2 + Bitarr1[1]
        T = Bitarr1[2] * 4 + Bitarr1[3] * 2 + Bitarr1[4] * 1
        i = i - 1
        X.append (S)
        X.append (T)
    return X


def makeTutlePos(Tur, n):
    X = []
    for i in range (n):
        temp = Tur[i].position ()
        temp = list (temp)
        X.append (temp[0])
    return X


def makeTrueTime_r(time_r):
    index = []
    time = []
    for j in range (0, 4):
        time.append (time_r[2 * j + 1])
    time.sort ()
    for i in range (4):
        for j in range (i, 4):
            if (time[i] == time_r[2 * j + 1]):
                swap (time_r[2 * j], time_r[2 * i])
                swap (time_r[2 * j + 1], time_r[2 * i + 1])


def swap(a, b):
    temp = a
    a = b
    b = temp


def maktIMove(valTurtle, step):
    event = eventRand ()
    min_s = 1
    max_s = 3
    currentDT = perf_counter ()
    time_r = [0, 0, 1, 0, 2, 0, 3, 0]
    road_l = step * 20
    flag = [1, 1, 1, 1]
    tur_set = [100, 70, 40, 10]
    rev_num_e = [0, 0, 0, 0]
    rev_num_f = [0, 0, 0, 0]
    rev_domb = [2, 0, 2, 1, 1, 1, 1, 1]
    rev_index = 1
    stun_num_e = [0, 0, 0, 0]
    stun_num_f = [0, 0, 0, 0]
    for i in range (4):
        rev_num_e[i] = randint (0, road_l - 10)
        rev_num_f[i] = randint (rev_num_e[i], rev_num_e[i] + 10)
        stun_num_e[i] = randint (0, road_l - 10)
        stun_num_f[i] = randint (rev_num_e[i], rev_num_e[i] + 10)
    endPos = -150 + 20 * step
    i = randint (0, min (rev_num_e))
    while (flag[0] == 1 or flag[1] == 1 or flag[2] == 1 or flag[3] == 1):
        speed = [randint (min_s, max_s), randint (min_s, max_s), randint (min_s, max_s), randint (min_s, max_s)]
        turRoadLengh = makeTutlePos (valTurtle, 4)
        i = i + 1
        for j in range (4):
            if (endPos - turRoadLengh[j] >= max_s):
                # Event reverse
                if ((0 == event[2 * j + 1] or event[2 * j + 1] == 1 or 0 == event[4 * j + 1] or event[
                    4 * j + 1] == 1) and (rev_num_f[event[2 * j]] > i > rev_num_e[event[2 * j]])):
                    if (1 == event[4 * j + 1] or event[4 * j + 1] == 2):
                        e_index = event[4 * j]
                    else:
                        e_index = event[2 * j]
                    rev_index = rev_index + 1
                    if (rev_domb[rev_index%5] == 2):
                        valTurtle[e_index].right (180)
                # Event stun
                if ((2 == event[2 * j + 1] or event[2 * j + 1] == 3) and (
                        stun_num_e[event[2 * j]] < i < stun_num_f[event[2 * j]])) or (
                        (2 == event[4 * j + 1] or event[4 * j + 1] == 3) and (
                        stun_num_e[event[4 * j]] < i < stun_num_f[event[4 * j]])):
                    if (3 == event[4 * j + 1] or event[4 * j + 1] == 4):
                        e_index = event[4 * j]
                    else:
                        e_index = event[2 * j]
                    if (j > e_index):
                        valTurtle[e_index].backward (speed[e_index])
                    speed[e_index] = 0
                    valTurtle[e_index].color (gencolor ())
                valTurtle[j].forward (speed[j])
            else:
                valTurtle[j].goto (endPos, tur_set[j])
                if (flag[j] == 1):
                    time_r[j * 2 + 1] = perf_counter ()
                    flag[j] = flag[j] - 1
    for j in range (4):
        time_r[2 * j + 1] = time_r[2 * j + 1] - currentDT
    makeTrueTime_r (time_r)
    return time_r
