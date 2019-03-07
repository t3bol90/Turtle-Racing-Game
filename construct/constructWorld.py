import time
from construct import createRoad, createTurtles, randomTurtles,createRanking

#n =

def createtheWorld(length):
	createRoad.create(length + 1)
	t = createTurtles.create()
	time.sleep(1)
	time_r = randomTurtles.makeItMove(t, length + 1)
	createRanking.create(time_r,t)
	