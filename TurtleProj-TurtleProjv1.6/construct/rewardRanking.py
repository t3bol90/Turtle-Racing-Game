from turtle import *
import os
import sys
def reward(root):
	cv = getcanvas()
	screen = getscreen()
	root.withdraw()
	os.system("creatUI.py")
	root.destroy()

	screen.bye()
