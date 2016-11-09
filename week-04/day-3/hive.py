from tkinter import *

def hive(): #it needs the number: how many hexgons are on each side

    root = Tk()

    w = 500
    h = 500
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    #coordinates and size of the first hexagon
    #x = 50
    #y = 100
    a = 20
    n = 6

    #create a hexagon:
    for j in range(0, n+1):
        if j <= n//2:
            p1 = 50
            p2 = 100 + j*(a*(3**0.5))

            for i in range(0, n//2+j+1):

                x = p1 + i*(a+a/2)
                y = p2 - i*(a*(3**0.5)/2)

                points = [[x, y], [x+a, y], [x+a+(a/2), y+(a*(3**0.5))/2], [x+a, y+a*(3**0.5)], [x, y+a*(3**0.5)], [x-(a/2), y+(a*(3**0.5))/2]]

                for k in range(len(points)-1):
                    canvas.create_line(points[k][0], points[k][1], points[k+1][0], points[k+1][1], fill='green')
                canvas.create_line(points[k+1][0], points[k+1][1], points[0][0], points[0][1], fill='green')
        else:
            p1 = 50 + (j-n//2)*(a+a/2)
            p2 = 100 + j*(a*(3**0.5))

            for i in range(0, i):

                x = p1 + i*(a+a/2)
                y = p2 - i*(a*(3**0.5)/2)

                points = [[x, y], [x+a, y], [x+a+(a/2), y+(a*(3**0.5))/2], [x+a, y+a*(3**0.5)], [x, y+a*(3**0.5)], [x-(a/2), y+(a*(3**0.5))/2]]

                for k in range(len(points)-1):
                    canvas.create_line(points[k][0], points[k][1], points[k+1][0], points[k+1][1], fill='green')
                canvas.create_line(points[k+1][0], points[k+1][1], points[0][0], points[0][1], fill='green')


    root.mainloop()

hive()
