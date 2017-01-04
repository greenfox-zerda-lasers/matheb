from tkinter import *
import time

root = Tk()
size = 800

canvas = Canvas(root, width=size, height=size)
canvas.pack()

ratio = 3**0.5

colors = ['SpringGreen2', 'DarkSeaGreen3', 'goldenrod1',  'PaleTurquoise1', 'coral1', 'maroon4',
    'DeepSkyBlue3', 'PaleTurquoise4', 'CadetBlue1', 'LightSalmon4', 'orange2',]

def triangles(x, y, a, n):
        time.sleep(0.03)
        canvas.create_polygon(x, y, x+a, y, x+(a/2), y+(ratio/2)*a, fill=colors[n*2-1], outline='black')
        canvas.update()
        if n > 0:
            triangles(x, y, a/2, n-1)
            triangles(x+(a/2), y, a/2, n-1)
            triangles(x+(a/4), y+(ratio/2)*a/2, a/2, n-1)




triangles(50, 20, 600, 5)
#creating_triangle(100, 150, 200)

root.mainloop()
