from tkinter import *

root = Tk()
size = 800

canvas = Canvas(root, width=size, height=size)
canvas.pack()

def creating_triangle(x, y, a):
    canvas.create_line(x, y, x+a, y)
    canvas.create_line(x+a, y, x+(a/2), y+((3**0.5)/2)*a)
    canvas.create_line(x+(a/2), y+((3**0.5)/2)*a, x, y)

def triangles(x, y, a, n):
        creating_triangle(x, y, a)
        if n > 0:
            triangles(x, y, a/2, n-1)
            triangles(x+(a/2), y, a/2, n-1)
            triangles(x+(a/4), y+((3**0.5)/2)*a/2, a/2, n-1)




triangles(100, 100, 400, 5)
#creating_triangle(100, 150, 200)

root.mainloop()
