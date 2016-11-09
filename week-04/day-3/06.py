# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *
def box_to_middle():


    root = Tk()

    w = 300
    h = 300
    
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    a = 20
    b = a

    line = canvas.create_polygon(m-(a/2), m-(b/2), m+(a/2), m-(b/2), m+(a/2), m+(b/2), m-(a/2), m+(b/2), fill='green')

    root.mainloop()

box_to_middle()
