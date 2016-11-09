# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *
def draw_box(x, y):


    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    a = 50
    b = a

    line = canvas.create_polygon(x, y, x+a, y, x+a, y+b, x, y+b, fill='green')

    root.mainloop()

draw_box(30, 50)
draw_box(100, 100)
draw_box(20, 250)
