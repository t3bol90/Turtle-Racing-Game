from turtle import *
from construct.createTurtles import gencolor


#Create road of course
def create(n):
	speed(0)
	penup()
	bgcolor("white")
	screensize(360, 100)
	#Set the default position
	if (n == 13):
		startPos = -120
	elif (n == 17):
		startPos = -160
	elif(n == 21):
		startPos = -200 
	goto(startPos, 40)
	#Draw lines of the road
	for step in range(n):
		write(step, align = 'center')
		right(90)
		#Draw dashed lines
		for step in range (15):
			forward(10)
			if (step % 2 == 0): penup()
			else: pendown()
		#Start drawing the next line
		penup()
		backward(150)
		left(90)
		forward(20)
