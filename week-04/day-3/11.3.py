# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

def draw_rainbow(a, steps): #a = size of the centered square

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    for i in range(((w-a)//steps), -1, -1):
        a = a - i*steps
        b = a
        RR=("%02x"%random.randint(0,255))
        GG=("%02x"%random.randint(0,255))
        BB=("%02x"%random.randint(0,255))
        ge="#"
        color=ge+RR+GG+BB
        line = canvas.create_polygon(m-(a/2), m-(b/2), m+(a/2), m-(b/2), m+(a/2), m+(b/2), m-(a/2), m+(b/2), fill=color)
    root.mainloop()

draw_rainbow(50, 6)
