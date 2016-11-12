from tkinter import *
import time
#from math import random, choice

root = Tk()
size = 900

canvas = Canvas(root, width=size, height=size)
canvas.pack()

def creating_hexagon(x, y, a):
    canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+(a*(3**0.5))/2, x+a, y+a*(3**0.5), x, y+a*(3**0.5), x-(a/2), y+(a*(3**0.5))/2, outline='black', fill='white')

def hexagons(x, y, a, n):
        time.sleep(0.05)
        creating_hexagon(x, y, a)
        canvas.update()
        if n > 0:
            hexagons(x, y, a/3, n-1)
            hexagons(x+2*(a/3), y, a/3, n-1)
            hexagons(x+2*(a/3), y+2*(a/3)*(3**0.5), a/3, n-1)
            hexagons(x, y+2*(a/3)*(3**0.5), a/3, n-1)
            hexagons(x+3*(a/3), y+(a/3)*(3**0.5), a/3, n-1)
            hexagons(x-(a/3), y+(a/3)*(3**0.5), a/3, n-1)

hexagons(400, 50, 300, 4)

root.mainloop()
