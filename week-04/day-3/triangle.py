from tkinter import *
import math
def triangulate(n): #it needs the number: how many triangle should be on the bottom


    root = Tk()

    w = 500
    h = 500
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    step = w / n

    for i in range(0, n):
        canvas.create_line(i*step, h, w/2+(i*(step/2)), (h-(w*(3**0.5)/2))+(i*(step*(3**0.5)/2)), fill='blue')
        canvas.create_line(w-(i*step)-1, h, w/2-(i*(step/2)), (h-(w*(3**0.5)/2))+(i*(step*(3**0.5)/2)), fill='blue')
        canvas.create_line(i*(step/2), h-(i*(step*(3**0.5)/2)), w-(i*(step/2)), h-(i*(step*(3**0.5)/2)), fill='blue')

    root.mainloop()

triangulate(5)
