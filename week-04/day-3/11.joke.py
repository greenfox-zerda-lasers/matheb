# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

def fill_square(a):

    root = Tk()

    w = 1000
    h = 600

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    for i in range(w//a):
        for j in range(h//b):
            RR=("%02x"%random.randint(0,255))
            GG=("%02x"%random.randint(0,255))
            BB=("%02x"%random.randint(0,255))
            ge="#"
            color=ge+RR+GG+BB
            canvas.create_polygon(i*a, j*b, (i+1)*a, 0+j*b, (i+1)*a, (j+1)*b, i*a, (j+1)*b, fill=color)

    root.mainloop()

root = Tk()

w = 1000
h = 600

canvas = Canvas(root, width=w, height=h)
canvas.pack()

    # Add a label, an entry, and a button to frame1
frame1 = Frame(root) # Create and add a frame to window
frame1.pack()

Label(framel,
    text = "How confused are you now in a scale of 1-10?: ").pack(side = LEFT)
order = StringVar()
entry = Entry(framel, textvariable = order,
              justify = RIGHT).pack(side = LEFT)
Button(frame1, text = "Why?",
    command = display).pack(side = LEFT)

m = w/2
b = a

def fill_square(order):

    for i in range(w//a):
        for j in range(h//b):
            RR=("%02x"%random.randint(0,255))
            GG=("%02x"%random.randint(0,255))
            BB=("%02x"%random.randint(0,255))
            ge="#"
            color=ge+RR+GG+BB
            canvas.create_polygon(i*a, j*b, (i+1)*a, 0+j*b, (i+1)*a, (j+1)*b, i*a, (j+1)*b, fill=color)

    root.mainloop()



draw_square(100, 'orange')
fill_square(3)
