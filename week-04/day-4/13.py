from tkinter import *
import random

root = Tk()
size = 500

canvas = Canvas(root, width=size, height=size)
canvas.pack()

ratio = 3**0.5

def hexa(x, y, a, n):
        if n == 0:
            return
        else:
            canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+a*ratio/2, x+a, y+a*ratio, x, y+a*ratio, x-(a/2), y+a*ratio/2, outline='black', fill='white')

            hexa(x, y, a/2, n-1)
            hexa(x+a/2+a/4, y+(a/2)*ratio/2, a/2, n-1)
            hexa(x, y+a/2*ratio, a/2, n-1)

hexa(100, 150, 200, 5)

root.mainloop()
