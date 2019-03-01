import time
from construct import createRoad, createTurtles, randomTurtles, createRanking

Length = createRoad.create()
t = createTurtles.create()
time.sleep(1)
randomTurtles.makeItMove(t, Length)
createRanking.create(t)
