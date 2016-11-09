# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

w = 300
h = 300
canvas = Canvas(root, width=w, height=h)
canvas.pack()

x = 20
y = 20
a = 100
b = 60

box_border1 = canvas.create_line(x, y, x+a, y, fill='blue')
box_border2 = canvas.create_line(x+a, y, x+a, y+b, fill='red')
box_border3 = canvas.create_line(x+a, y+b, x, y+b, fill='yellow')
box_border4 = canvas.create_line(x, y+b, x, y, fill='skyblue')

root.mainloop()
