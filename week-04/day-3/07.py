# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *
def fill_with_rectangles(a, b):


    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    line = canvas.create_polygon(0, 0, a, 0, a, b, 0, b, fill="#c9f3ff")
    line = canvas.create_polygon(a+1, 0, w, 0, w, b, a+1, b, fill="#1289aa")
    line = canvas.create_polygon(0, b+1, a, b+1, a, h, 0, h, fill='lightgrey')
    line = canvas.create_polygon(a+1, b+1, w, b+1, w, h, a+1, h, fill='skyblue')

    root.mainloop()

fill_with_rectangles(120, 60)
