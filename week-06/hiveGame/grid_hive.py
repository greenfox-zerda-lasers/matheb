from tkinter import *
import time
import random
import pygame
import sys

root = Tk()
w = 1000
h = 600
canvas = Canvas(root, width=w, height=h, bg="black")
canvas.pack()
canvas.create_text(800, 100, text="The HIVE", font=('Helvetica', 50), fill='skyblue')
canvas.create_text(800, 300, text="Choose one of the hexagons\nand click on it.\nThe tiny little bees will\nrebuild their hive for you.", font=('Helvetica', 20), fill='medium aquamarine')

class Game():

    ratio = 3**0.5

    def __init__(self, n):
        self.level = n
        #root.bind('<Button-1>', self.click)

    def initNewLevel(self):
        self.level += 1

    def creating_hexagon(self, x, y, a, j, i):
        position = [j, i]
        color = ['white', 'yellow', 'white', 'yellow']
        filling = color[random.randint(0,1)]
        hexa = canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+a*self.ratio/2, x+a, y+a*self.ratio, x, y+a*self.ratio, x-(a/2), y+a*self.ratio/2, outline='black', fill=filling, tags=[position, filling, 'hexa'])
        print(position)


    def board_coord(self, n, x0, y0, a):
        emptyBoard = [['null']*n for _ in range(n)]
        tilesCenter = [['null']*n for _ in range(n)]
        #self.tilescolor = [['null']*n for _ in range(n)]
        for j in range(len(emptyBoard)):
            for i in range(len(emptyBoard[j])):
                if j <= n//2:
                    p1 = x0
                    p2 = y0 + j*(a*(3**0.5))

                    #creating one line
                    for i in range(0, n//2+j+1):
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        emptyBoard[j][i] = [x, y]
                        tilesCenter[j][i] = [x+a/2, y+(a*self.ratio/2)]

                else:
                    #while the lines are shorter
                    p1 = x0 + (j-n//2)*(a+a/2)
                    p2 = y0 + (j+n//2+1)*(a*self.ratio/2) - a*(self.ratio/2)


                    for i in range(n-(j-n//2)):
                        #creating one line
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        emptyBoard[j][i] = [x, y]
                        tilesCenter[j][i] = [x+a/2, y+(a*self.ratio/2)]

        #yield tilesCenter
        return emptyBoard

        #print(emptyBoard)

    def hive(self, n, x0, y0, a):
        for j in range(len(self.board_coord(n, x0, y0, a))):
            for i in range(len(self.board_coord(n, x0, y0, a)[j])):
                if self.board_coord(n, x0, y0, a)[j][i] != 'null' :
                    x = self.board_coord(n, x0, y0, a)[j][i][0]
                    y = self.board_coord(n, x0, y0, a)[j][i][1]
                    time.sleep(0.1)
                    #color = 1
                    self.creating_hexagon(x, y, a, j, i)
                    canvas.update()
        #self.click()

        canvas.mainloop()

    def click(self):
        if canvas.find_withtag(CURRENT):
            #self.identify('event')
            print(canvas.gettags(CURRENT))
            pos = canvas.gettags(CURRENT)[0]
            color = canvas.gettags(CURRENT)[1]
            if color == 'yellow':
                canvas.itemconfig(ALL, fill='white')
            elif color == 'white':
                canvas.itemconfig(ALL, fill='yellow')
            #if pos[0] < n//2:
            """elif canvas.gettags(str(int(pos[0])-1)+" "+str(int(pos[2])))[1] == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])-1)+" "+str(int(pos[2]))), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])-1)+" "+str(int(pos[2]))), fill="white")
            if canvas.gettags(str(int(pos[0]))+" "+str(int(pos[2])-1))[1] == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0]))+" "+str(int(pos[2])-1)), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0]))+" "+str(int(pos[2])-1)), fill="white")
            if canvas.gettags(str(int(pos[0])-1)+" "+str(int(pos[2])-1)) == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])-1)+" "+str(int(pos[2])-1)), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])-1)+" "+str(int(pos[2])-1)), fill="white")
            if canvas.gettags(str(int(pos[0])+1)+" "+str(int(pos[2])+1)) == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])+1)+" "+str(int(pos[2])+1)), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])+1)+" "+str(int(pos[2])+1)), fill="white")
            if canvas.gettags(str(int(pos[0])+1)+" "+str(int(pos[2]))) == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])+1)+" "+str(int(pos[2]))), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0])+1)+" "+str(int(pos[2]))), fill="white")
            if canvas.gettags(str(int(pos[0]))+" "+str(int(pos[2])+1)) == 'white':
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0]))+" "+str(int(pos[2])+1)), fill="yellow")
            else:
                canvas.itemconfig(canvas.find_withtag(str(int(pos[0]))+" "+str(int(pos[2])+1)), fill="white")"""
            #elif pos[0] == n//2:

            #elif pos[0] > n//2:
            #canvas.itemconfig(self.identify('<Button-1>'), fill="blue")
            canvas.update_idletasks()
            canvas.after(200)
            #canvas.itemconfig(CURRENT, fill="red")

    root.bind('<Button-1>', click)

    """def identify(self, event):
    item = canvas.find_closest(event.x, event.y)
    tags = canvas.gettags(item)
    return item
root.bind("<Button-1>", identify)"""

game = Game(7)
game.hive(9, 100, 150, 30)
