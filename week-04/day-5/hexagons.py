from tkinter import *

root = Tk()
size = 900

canvas = Canvas(root, width=size, height=size)
canvas.pack()

def creating_hexagon(x, y, a):
    points = [[x, y], [x+a, y], [x+a+(a/2), y+(a*(3**0.5))/2], [x+a, y+a*(3**0.5)], [x, y+a*(3**0.5)], [x-(a/2), y+(a*(3**0.5))/2]]
    for k in range(len(points)-1):
        canvas.create_line(points[k][0], points[k][1], points[k+1][0], points[k+1][1], fill='green')
    canvas.create_line(points[k+1][0], points[k+1][1], points[0][0], points[0][1], fill='green')

def hexagons(x, y, a, n):
        creating_hexagon(x, y, a)
        if n > 0:
            hexagons(x, y, a/3, n-1)
            hexagons(x+2*(a/3), y, a/3, n-1)
            hexagons(x+2*(a/3), y+2*(a/3)*(3**0.5), a/3, n-1)
            hexagons(x, y+2*(a/3)*(3**0.5), a/3, n-1)
            hexagons(x+3*(a/3), y+(a/3)*(3**0.5), a/3, n-1)
            hexagons(x-(a/3), y+(a/3)*(3**0.5), a/3, n-1)

hexagons(200, 50, 300, 4)

root.mainloop()
