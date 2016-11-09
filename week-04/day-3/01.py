# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

w = 300
h = 300
canvas = Canvas(root, width=w, height=h)
canvas.pack()

red_line = canvas.create_line(0, w/2, h, w/2, fill='red')
green_line = canvas.create_line(h/2, 0, h/2, w, fill='green')

root.mainloop()
