# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import *

root = Tk()

w = 300
h = 300
canvas = Canvas(root, width=w, height=h)
canvas.pack()

first = canvas.create_line(0, 0, w, h, fill='green')
second = canvas.create_line(0, h, w, 0, fill='green')

root.mainloop()
