from tkinter import *

def hive(n, x0, y0, a): #it needs
                        #the number(n): how many hexgons are on each side
                        #the first hexagons top left position (x0, y0)
                        #and the hexagon's side length (a)
    root = Tk()
    w = 500
    h = 500
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    #create the hive:
    for j in range(0, (n//2)*2+1):
        #while it is bigger and bigger
        if j <= n//2:
            p1 = x0
            p2 = y0 + j*(a*(3**0.5))

            #creating one line
            for i in range(0, n//2+j+1):
                x = p1 + i*(a+a/2)
                y = p2 - i*(a*(3**0.5)/2)
                #the list of the points of the hexagon
                points = [[x, y], [x+a, y], [x+a+(a/2), y+(a*(3**0.5))/2], [x+a, y+a*(3**0.5)], [x, y+a*(3**0.5)], [x-(a/2), y+(a*(3**0.5))/2]]

                #creating one hexagon
                for k in range(len(points)-1):
                    canvas.create_line(points[k][0], points[k][1], points[k+1][0], points[k+1][1], fill='green')
                canvas.create_line(points[k+1][0], points[k+1][1], points[0][0], points[0][1], fill='green')

        else:
            p1 = x0 + (j-n//2)*(a+a/2)
            p2 = y0 + (j+n//2+1)*(a*(3**0.5)/2) - a*((3**0.5)/2)

            for i in range(0, i):

                x = p1 + i*(a+a/2)
                y = p2 - i*(a*(3**0.5)/2)

                points = [[x, y], [x+a, y], [x+a+(a/2), y+(a*(3**0.5))/2], [x+a, y+a*(3**0.5)], [x, y+a*(3**0.5)], [x-(a/2), y+(a*(3**0.5))/2]]

                for k in range(len(points)-1):
                    canvas.create_line(points[k][0], points[k][1], points[k+1][0], points[k+1][1], fill='green')
                canvas.create_line(points[k+1][0], points[k+1][1], points[0][0], points[0][1], fill='green')


    root.mainloop()

hive(30, 50, 100, 10)
hive(5, 50, 100, 30)
