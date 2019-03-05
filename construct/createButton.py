from tkinter import Tk, Button
from construct.createRoad import *

#Create road's length buttons
def selectLength():
    win = Tk()
    win.tittle("Turtles' Race")
    win.geometry("250x150+300+300")

    columnconfigure(0, pad=3)
    columnconfigure(1, pad=3)
    columnconfigure(2, pad=3)

    rowconfigure(0, pad=3)
    rowconfigure(1, pad=3)

    longButton = Button(win, text = "Long", command = createRoad.createLong())
    longButton.grid(row = 1, column = 0)
    mediumButton = Button(win, text = "Medium", command = createRoad.createMedium())
    mediumButton.grid(row = 1, column = 1)
    shortButton = Button(win, text = "Short", command = createRoad.createShort())
    shortButton.grid(row = 1, column = 2)
    win.mainloop()
