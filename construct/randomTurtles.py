from turtle import *
from random import randint, shuffle
from random import random
from construct.createTurtles import gencolor
from time import perf_counter


# Apply de Bruijn sequence to create events of turtles
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


#
def makeTutlePos(Tur, n):
    X = []
    for i in range (n):
        temp = Tur[i].position ()
        temp = list (temp)
        X.append (temp[0])
    return X

#Sort list of turtle's index and time records
def makeTrueTime_r(time_r):
    index = []
    time = []
    for j in range (4):
        time.append (time_r[2 * j + 1])
    time.sort (reverse = True)
    for i in range (4):
        for j in range (i, 4):
            if (time[i] == time_r[2 * j + 1]):
                #Swap index
                temp = time_r[2 * j]
                time_r[2 * j] = time_r[2 * i]
                time_r[2 * i] = temp
                #Swap time
                temp = time_r[2 * j + 1]
                time_r[2 * j + 1] = time_r[2 * i + 1]
                time_r[2 * i + 1] = temp

# Sort list of turtle's index and time records
def makeTrueTime_r(time_r):
    index = []
    time = []
    for j in range (4):
        time.append (time_r[2 * j + 1])
    time.sort (reverse=True)
    for i in range (4):
        for j in range (i, 4):
            if (time[i] == time_r[2 * j + 1]):
                # Swap index
                temp = time_r[2 * j]
                time_r[2 * j] = time_r[2 * i]
                time_r[2 * i] = temp
                # Swap time
                temp = time_r[2 * j + 1]
                time_r[2 * j + 1] = time_r[2 * i + 1]
                time_r[2 * i + 1] = temp


# Making random events
def makeItMove(valTurtle, step):
    event = eventRand ()
    minSpeed = 1
    maxSpeed = 3
    StartTime = perf_counter ()
    RankTimeTable = [0, 0, 1, 0, 2, 0, 3, 0]
    road_l = step * 20
    flag = [1, 1, 1, 1]
    SetTurPosition = [100, 70, 40, 10]
    stunIndex = [0,0,0,0]
    stunStep = 6
    revStep = 6
    endPos = -150 + road_l
    pos0 = [randint(-140,endPos),randint(-140,endPos),randint(-140,endPos),randint(-140,endPos)]
    pos1 = [randint(-140,endPos),randint(-140,endPos),randint(-140,endPos),randint(-140,endPos)]
    pos2 = [randint(-140,endPos),randint(-140,endPos),randint(-140,endPos),randint(-140,endPos)]
    while (flag[0] == 1 or flag[1] == 1 or flag[2] == 1 or flag[3] == 1):
        speed = [randint (minSpeed, maxSpeed), randint (minSpeed, maxSpeed), randint (minSpeed, maxSpeed), randint (minSpeed, maxSpeed)]
        turRoadLengh = makeTutlePos (valTurtle, 4)
        TurtleEventFlag = [1, 1, 1, 1]
        for i in range(8): #Check event
            #If event is stun
            if((event[i*2+1]==0  and (pos0[event[2*i]]-maxSpeed)< turRoadLengh[event[i*2]] < pos0[event[2*i]])or (event[2*i+1]==1 and (pos1[event[2*i]]-maxSpeed)<turRoadLengh[event[i*2]]<pos1[event[2*i]])):
                TurtleEventFlag[event[i*2]] = 0
                valTurtle[event[2*i]].color(gencolor())
                stunIndex[event[i*2]] = stunIndex[event[i*2]] + 1
                if (stunIndex[event[i*2]] % stunStep == 0):
                    TurtleEventFlag[event[i * 2]] = 1
            #If event is backward
            if((event[i*2+1]==2 or event[i*2+1]==3)and(pos2[event[i*2]] - maxSpeed< turRoadLengh[event[i*2]] < pos2[event[i*2]])):
                TurtleEventFlag[event[i*2]] = -1
###Make a real move and do event act
        for j in range (4):
            if (endPos - turRoadLengh[j] >= maxSpeed):
                if (TurtleEventFlag[j]==1):
                    valTurtle[j].forward (speed[j])

                if (TurtleEventFlag[j] == -1):
                    valTurtle[j].left (180)
                    pos2[j] = pos2[j] - speed[j]*revStep
            else:
                valTurtle[j].goto (endPos, SetTurPosition[j])
                if (flag[j] == 1):
                    RankTimeTable[j * 2 + 1] = perf_counter ()
                    flag[j] = flag[j] - 1

    for j in range (4):
        RankTimeTable[2 * j + 1] = RankTimeTable[2 * j + 1] - StartTime
    makeTrueTime_r (RankTimeTable)
    return RankTimeTable
