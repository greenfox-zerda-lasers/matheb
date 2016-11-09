# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *
def draw_square(a):


    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    m = w/2
    b = a

    line = canvas.create_polygon(m-(a/2), m-(b/2), m+(a/2), m-(b/2), m+(a/2), m+(b/2), m-(a/2), m+(b/2), fill='green')

    root.mainloop()

for i in range(21):
    draw_square(20+2*i)
