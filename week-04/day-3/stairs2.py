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
    s = a
    first = 0
    second = 0

    for i in range(0, n+1):
        line = canvas.create_polygon(first, second, first+s, second, first+s, i*b+s, i*a, i*b+s, fill='purple')
        first = i*a+s
        second = i*b+s
        s += 5
    root.mainloop()

draw_stairs(10, 30)
