# create a 300x300 canvas.
# fill it with a checkerboard pattern.
from tkinter import *

def checkerboard():

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    a = w//8
    b = a

    for i in range(8):
        for j in range(8):
            if i%2 == j%2:
                canvas.create_polygon(i*a, j*b, (i+1)*a, 0+j*b, (i+1)*a, (j+1)*b, i*a, (j+1)*b, fill='black')

    root.mainloop()

checkerboard()
