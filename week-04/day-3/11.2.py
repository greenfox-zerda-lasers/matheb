# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random
#import webcolors

def draw_square(a, color):

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    line = canvas.create_polygon(m-(a/2), m-(b/2), m+(a/2), m-(b/2), m+(a/2), m+(b/2), m-(a/2), m+(b/2), fill=color)
    root.mainloop()

"""def rgb():
   return webcolors.rgb_to_hex([random.randrange(0,256) for _ in range(3)])"""

def fill_square(a):

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    for i in range(w//a):
        for j in range(h//b):
            RR=("%02x"%(220-i*15))
            GG=("%02x"%(j*10+60))
            BB=("%02x"%(255-i*10))
            ge="#"
            color=ge+RR+GG+BB
            canvas.create_polygon(i*a, j*b, (i+1)*a, 0+j*b, (i+1)*a, (j+1)*b, i*a, (j+1)*b, fill=color)


    root.mainloop()


#draw_square(100, 'orange')
fill_square(20)
