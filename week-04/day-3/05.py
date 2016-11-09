# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *
def draw_line(x, y):


    root = Tk()

    w = 300
    h = 300
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    line = canvas.create_line(x, y, x+50, y, fill='green')

    root.mainloop()

draw_line(20, 30)
draw_line(150, 30)
draw_line(50, 200)
