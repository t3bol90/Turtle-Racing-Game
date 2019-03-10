from turtle import *
from tkinter import *
from construct import rewardRanking
from construct.createTurtles import gencolor
import time

def create(timeindex, tur, col):
	# Clear drawer's line and pen-it-up
	cv = getcanvas()
	screen = getscreen()
	Bgphoto = PhotoImage(file = "images/race/BGTurtleBlack.gif", master = cv)
	cv.create_image(-360, -300, image = Bgphoto, anchor = N+W)
	cv.image = Bgphoto
	clear ()
	pu ()
	# Clear turtles' lines
	for i in range (4):
		tur[timeindex[2 * i]].clear ()
	# Penup turtles
	for i in range (4):
		tur[timeindex[2 * i]].pu ()
	# Hide turtles
	for i in range (4):
		tur[timeindex[2 * i]].ht ()
	#Medals
	textID = cv.create_text(0, -180, text = "RECORD", font = ("Fipps",18,"italic"), fill = "#ffffff")
	# Draw the ranking
	ht ()
	y = 100
	setpos (-220, y)
	pd ()
	for i in range (3):
		forward (480)
		pu ()
		y -= 100
		goto (-220, y)
		pd ()
	pu ()
	x = -220
	setpos (x, 100)
	pd ()
	right (90)
	forward (200)
	for i in range (4):
		pu ()
		x += 120
		goto (x, 100)
		pd ()
		forward (200)
	# Write something :v
	pu ()
	goto (-280, 40)
	write ("Turtle", move=False, align="center", font=("Fipps", 15, "normal"))
	goto (-280, -60)
	write ("Time", move=False, align="center", font=("Fipps", 15, "normal"))
	# Turtle's rank
	x = -160
	for i in range (4):
		tur[timeindex[2 * i]].color(col[timeindex[2 * i]])
		tur[timeindex[2 * i]].goto (x, 50)
		tur[timeindex[2 * i]].left (90)
		x += 120
		tur[timeindex[2 * i]].st ()
	x = -165
	for i in range (4):
		goto (x, -55)
		x += 120
		write (("%0.2f" % timeindex[2 * i + 1]), move=False, align="center", font=("Arial", 10, "bold"))
	#Continue
	###Clear 2,3,4 turtle:
	time.sleep(3)
	cv.delete(textID)
	Bgphoto = PhotoImage(file = "images/reward_medals/Ranking.gif", master = cv)
	cv.create_image(-360, -300, image = Bgphoto, anchor = N+W)
	cv.image = Bgphoto
	tur[timeindex[6]].clear()
	tur[timeindex[6]].ht()
	clear()
	tur[timeindex[0]].right(90)
	tur[timeindex[0]].forward(150)
	tur[timeindex[0]].left(90)
	tur[timeindex[0]].backward(50)
	tur[timeindex[2]].right(90)
	tur[timeindex[2]].forward(160)
	tur[timeindex[2]].left(90)
	tur[timeindex[2]].backward(135)
	tur[timeindex[4]].left(90)
	tur[timeindex[4]].forward(215)
	tur[timeindex[4]].right(90)
	tur[timeindex[4]].backward(165)
	flag = 3
	temp = Turtle ()
	temp.penup ()
	temp.ht ()
	while(flag):
		for i in range(1,13):
			cv = getcanvas()
			dir1Image = "images/reward_medals/F"
			dir1Image = dir1Image + str(i)
			dir1Image = dir1Image + ".png"
			dir2Image = "images/reward_medals/S"
			dir2Image = dir2Image + str(i)
			dir2Image = dir2Image + ".png"
			dir3Image = "images/reward_medals/T"
			dir3Image = dir3Image + str(i)
			dir3Image = dir3Image + ".png"
			Medal1 = PhotoImage(file = dir3Image, master = cv)
			cv.create_image(-250, -50, image = Medal1, anchor = N+W)
			cv.image = Medal1
			Medal2 = PhotoImage(file = dir1Image, master = cv)
			cv.create_image(-70, -190, image = Medal2, anchor = N+W)
			cv.image = Medal2
			Medal3 = PhotoImage(file = dir2Image, master = cv)
			cv.create_image(85, -110, image = Medal3, anchor = N+W)
			cv.image = Medal3
			tur[timeindex[0]].forward(50)
			tur[timeindex[0]].backward(50)
			tur[timeindex[0]].color(gencolor())
			tur[timeindex[2]].forward(50)
			tur[timeindex[2]].backward(50)
			tur[timeindex[4]].forward(50)
			tur[timeindex[4]].backward(50)
			temp.speed(1)
			temp.forward(12)
		flag = flag - 1
