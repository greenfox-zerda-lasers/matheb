# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *
def draw_to_middle(x, y):


    root = Tk()

    w = 300
    h = 300
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    line = canvas.create_line(x, y, w/2, h/2, fill='green')

    root.mainloop()


draw_to_middle(20, 30)
draw_to_middle(150, 30)
draw_to_middle(50, 200)
