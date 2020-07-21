from tkinter import *
from turtle import *
from Alphaproj import *

#--------------------------------------------------------------------#
#Set main window
root = Tk()
root.geometry("800x600+300-80")
root.title("Turtle Racing Boiz")
#--------------------------------------------------------------------#
#Set select buttons window
select = Tk()
select.withdraw()
select.title("Road's Length")
#--------------------------------------------------------------------#
#Create road's length buttons
def makeshort(event, frame):
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(12)
	root.deiconify()
def makelong(event, frame):
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(20)
	root.deiconify()
def makemedium(event, frame):
	select.withdraw()
	frame.destroy()
	clearscreen()
	createtheWorld(16)
	root.deiconify()
#Choose length
def selectLength(event):
	#Hide old window
	root.withdraw()
	#Frame contains select buttons
	selectframe = Frame(select)
	selectframe.pack(fill = BOTH)
	text = Label(selectframe, text = "Select the length of the road:")
	text.grid(row = 0, columnspan = 3)
	lengthbutton1 = Button(selectframe, text = "Short")
	lengthbutton1.bind("<Button-1>", lambda event: makeshort(event, selectframe))
	lengthbutton1.grid(row = 1, column = 0, columnspan = 1)
	lengthbutton2 = Button(selectframe, text = "Medium")
	lengthbutton2.bind("<Button-1>", lambda event: makemedium(event, selectframe))
	lengthbutton2.grid(row = 1, column = 1, columnspan = 1)
	lengthbutton3 = Button(selectframe, text = "Long")
	lengthbutton3.bind("<Button-1>", lambda event: makelong(event, selectframe))
	lengthbutton3.grid(row = 1, column = 2, columnspan = 1)
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
