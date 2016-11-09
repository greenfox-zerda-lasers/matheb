# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *
import random
def draw_to_middle(n):


    root = Tk()

    w = 300
    h = 300
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    for i in range(w//n+1):
        RR=("%02x"%random.randint(0,255))
        GG=("%02x"%random.randint(0,255))
        BB=("%02x"%random.randint(0,255))
        ge="#"
        color=ge+RR+GG+BB
        canvas.create_line(i*n, 0, w/2, h/2, fill=color)
        canvas.create_line(0, i*n, w/2, h/2, fill=color)
        canvas.create_line(w, i*n, w/2, h/2, fill=color)
        canvas.create_line(i*n, h, w/2, h/2, fill=color)

    root.mainloop()

draw_to_middle(10)
