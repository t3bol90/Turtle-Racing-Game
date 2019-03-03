from turtle import *


def create(timeindex, tur):
    # Clear drawer's line and pen-it-up
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
    write ("Turtle", move=False, align="center", font=("Arial", 15, "normal"))
    goto (-280, -60)
    write ("Time", move=False, align="center", font=("Arial", 15, "normal"))
    # Turtle's rank
    x = -160
    for i in range (4):
        tur[timeindex[2 * i]].goto (x, 50)
        tur[timeindex[2 * i]].left (90)
        x += 120
        tur[timeindex[2 * i]].st ()
    x = -165
    for i in range (4):
        goto (x, -55)
        x += 120
        write (("%0.2f" % timeindex[2 * i + 1]), move=False, align="center", font=("Arial", 10, "bold"))
