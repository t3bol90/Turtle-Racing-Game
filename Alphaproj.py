import time
from construct import createRoad, createTurtles, randomTurtles

length = createRoad.create()
t = createTurtles.create()
time.sleep(1)
randomTurtles.maktIMove(t, length)