import time
from construct import createRoad, createTurtles, randomTurtles,createRanking, createButton

selectLength()
length = createRoad.create()
t = createTurtles.create()
time.sleep(1)
time_r = randomTurtles.makeItMove(t, length)
createRanking.create(time_r,t)
