from tkinter import *
from turtle import *
from construct.constructWorld import *

#--------------------------------------------------------------------#
#Set main window
root = Tk()
root.geometry("800x600+300-80")
root.title("Turtle Racing Boiz")
root.iconbitmap(default = "images/icon/Turtle.ico")
#--------------------------------------------------------------------#
#Set select buttons window
select = Tk()
select.withdraw()
select.geometry("545x115+450-280")
select.title("Road's Length")
#--------------------------------------------------------------------#
#Create road's length buttons
def makeshort(event, frame):
	root.withdraw()
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(12)
	root.deiconify()
def makelong(event, frame):
	root.withdraw()
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(20)
	root.deiconify()
def makemedium(event, frame):
	root.withdraw()
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(16)
	root.deiconify()
#Choose length
def selectLength(event):
	#Frame contains select buttons
	selectframe = Frame(select, bg = "#f2cf8d")
	selectframe.pack(fill = BOTH)
	#Select text
	selectphoto = PhotoImage(file = "images/select/chooseLength.png", master = selectframe)
	text = Label(selectframe, image = selectphoto)
	text.image = selectphoto #This is really annoying when Python uses its garbage-collector :<
	text.grid(row = 0, columnspan = 3)
	#Button Butts :>
	#Short
	buttonphoto1 = PhotoImage(file = "images/select/ButtonShort.png", master = selectframe)
	lengthbutton1 = Button(selectframe, image = buttonphoto1)
	lengthbutton1.image = buttonphoto1
	lengthbutton1.bind("<Button-1>", lambda event: makeshort(event, selectframe))
	lengthbutton1.grid(row = 1, column = 0, sticky=N+E+S+W)
	#Medium
	buttonphoto2 = PhotoImage(file = "images/select/ButtonMedium.png", master = selectframe)
	lengthbutton2 = Button(selectframe, image = buttonphoto2)
	lengthbutton2.image = buttonphoto2
	lengthbutton2.bind("<Button-1>", lambda event: makemedium(event, selectframe))
	lengthbutton2.grid(row = 1, column = 1, sticky=N+E+S+W)
	#Long
	buttonphoto3 = PhotoImage(file = "images/select/ButtonLong.png", master = selectframe)
	lengthbutton3 = Button(selectframe, image = buttonphoto3)
	lengthbutton3.image = buttonphoto3
	lengthbutton3.bind("<Button-1>", lambda event: makelong(event, selectframe))
	lengthbutton3.grid(row = 1, column = 2, sticky=N+E+S+W)
	#Deiconify select window
	select.deiconify()
#--------------------------------------------------------------------#
#Set background
bgframe = Frame(root)
bgframe.pack(fill = BOTH)
#Background
bgphoto = PhotoImage(file = "images/login/Background.png")
background = Label(bgframe, image = bgphoto)
background.pack()
#Play button
playbutton = PhotoImage(file = "images/login/PlayButton.png")
play = Button(background, image = playbutton)
play.bind("<Button-1>", selectLength)
play.place(x = 135, y = 430)
#Quit button
quitbutton = PhotoImage(file = "images/login/QuitButton.png")
quit = Button(background, image = quitbutton, command = bgframe.quit)
quit.place(x = 245, y = 515)
#--------------------------------------------------------------------#
#Main loop
root.mainloop()
