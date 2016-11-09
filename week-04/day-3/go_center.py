# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *
def draw_to_middle():


    root = Tk()

    w = 300
    h = 300
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    for i in range(w//20):
        canvas.create_line(i*20, 0, w/2, h/2, fill='green')
        canvas.create_line(0, i*20, w/2, h/2, fill='green')
        canvas.create_line(w, i*20, w/2, h/2, fill='green')
        canvas.create_line(i*20, h, w/2, h/2, fill='green')

    root.mainloop()

draw_to_middle()
