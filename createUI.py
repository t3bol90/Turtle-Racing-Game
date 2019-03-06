from tkinter import *
from Alphaproj import *

#--------------------------------------------------------------------#
#Set windows
root = Tk()
root.geometry("800x600+300-80")
root.title("Turtle Racing Boiz")
#--------------------------------------------------------------------#
def constructor(event):
	root.destroy()
	createtheWorld()
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
play.bind("<Button-1>", constructor)
play.place(x = 135, y = 430)
#Quit button
quitbutton = PhotoImage(file = "images/login/QuitButton.png")
quit = Button(background, image = quitbutton, command = bgframe.quit)
quit.place(x = 245, y = 515)
#--------------------------------------------------------------------#
#Main loop
root.mainloop()
