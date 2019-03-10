from turtle import *
from random import randint


#Generate colours of turtles
def gencolor():
	r = lambda: randint(0, 255)
	return ('#%02X%02X%02X' % (r(), r(), r()))


#Create turtles absolutely
def create(n):
	#Set the default coordinates
	if (n == 13):
		x, y, spin = -130, 0, 0
	elif (n == 17):
		x, y, spin = -170, 0, 0
	elif (n == 21):
		x, y, spin = -210, 0, 0

	tur = []
	color = []
	register_shape ("fish", ((-4, 3), (-4, 1), (-2, 2), (0, 4), (2, 2), (4, 3), (4, 1), (2, 2), (0, -2), (-1, -3), (1, -3), (-2, 2)))
	register_shape("pacman", ((5.88,8.09),(3.09,9.51),(0,10),(-3.09,9.51),(-5.88,8.09),(-8.09,5.88),(-9.51,3.09),(-10,0),(-9.51,-3.09),(-8.09,-5.88),(-5.88,-8.09),(-3.09,-9.51),(0,-10),(3.09,-9.51),(5.88,-8.09),(8.09,-5.88),(0,0),(5.88,8.09)))
	register_shape("mouse",((-5,-5),(-2.5,-5),(-2.5,0),(-2.5,-2.5),(2.5,-2.5),(2.5,-5),(-5,0),(-2.5,0),(5,-5),(5,0),(2.5,0),(0,5),(-2.5,0)))
	register_shape("cat",((10,0),(9.51,3.09),(11,11),(3.09,9.51),(5.88,8.09),(8.09,5.88),(5.88,8.09),(3.09,9.51),(0,10),(-3.09,9.51),(-5.88,8.09),(-8.09,5.88),(-9.51,3.09),(-11,11),(-3.09,9.51),(-5.88,8.09),(-8.09,5.88),(-9.51,3.09),(-10,0),(-9.51,-3.09),(-8.09,-5.88),(-5.88,-8.09),(-3.09,-9.51),(-0.00,-10.00),(3.09,-9.51),(5.88,-8.09),(8.09,-5.88),(9.51,-3.09)))
	r_shape = 'turtle'
	while (1):
		try:
			r_shape = str (textinput ("Choose character", "Please choose your character (turtle,fish,pacman,)"))
			break
		except (RuntimeError, TypeError, NameError, TurtleGraphicsError):
			r_shape = 'turtle'
	for n in (gencolor(),gencolor(),gencolor(),gencolor()):	  #Create the turtles
	#Customize the turtles
		t = Turtle()
		# bluebear = "images/characters/set1/Bluebearforward.gif"
		t.color(n)
		t.shape(r_shape)
		if r_shape == 'pacman':
			t.shapesize(1, 1, 1)
		if r_shape == 'fish' or r_shape == "mouse":
			t.shapesize(3,3,1)

	#Move turtles to the start point
		t.penup()
		t.goto(x,y)
		t.pendown()
		y -= 30

	#Spin each turtle
		spin += 1
		if (spin % 2 == 0):
			t.right(360)
		else:
			t.left(360)

		tur.append(t)
		color.append(n)

	return tur,color	#Return the list of turtles
