from tkinter import *
import random

def draw_stairs(a, n):

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    for i in range(0, n+1):
        line = canvas.create_polygon(i*a, i*b, i*a+a, i*b, i*a+a, i*b+b, i*a, i*b+b, fill='purple')
    root.mainloop()

draw_stairs(10, 30)
