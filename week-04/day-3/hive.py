from tkinter import *
import time
import random

root = Tk()
w = 1000
h = w
canvas = Canvas(root, width=w, height=h)
canvas.pack()
ratio = 3**0.5

def creating_hexagon(x, y, a):
    color = ['white', 'yellow', 'white', 'yellow']
    canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+a*ratio/2, x+a, y+a*ratio, x, y+a*ratio, x-(a/2), y+a*ratio/2, outline='black', fill=color[random.randint(0,1)])

def hive(n, x0, y0, a): #it needs
                        #the number(n): how many rows are in the big hexagon
                        #the first hexagons top left position (x0, y0)
                        #and the hexagon's side length (a)

    #create the hive:
    for j in range(0, (n//2)*2+1):
        #while it is bigger and bigger
        if j <= n//2:
            p1 = x0
            p2 = y0 + j*(a*(3**0.5))

            #creating one line
            for i in range(0, n//2+j+1):
                x = p1 + i*(a+a/2)
                y = p2 - i*(a*ratio/2)
                time.sleep(0.1)
                creating_hexagon(x, y, a)
                canvas.update()

        else:
            #while the lines are shorter
            p1 = x0 + (j-n//2)*(a+a/2)
            p2 = y0 + (j+n//2+1)*(a*ratio/2) - a*(ratio/2)

            for i in range(0, i):
                #creating one line
                x = p1 + i*(a+a/2)
                y = p2 - i*(a*ratio/2)
                time.sleep(0.1)
                creating_hexagon(x, y, a)
                canvas.update()

hive(13, 100, 150, 20)

root.mainloop()
