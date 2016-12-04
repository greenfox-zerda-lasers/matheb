from tkinter import *
import time
import random

root = Tk()
w = 1000
h = 600
canvas = Canvas(root, width=w, height=h, bg='#146372')
canvas.pack()
canvas.create_text(800, 100, text="The HIVE", font=('Helvetica', 50), fill='#eafbff')
canvas.create_text(800, 300, text="Choose one of the hexagons\nand click on it.\nThe tiny little bees will\nrebuild their hive for you.", font=('Helvetica', 20), fill='#eafffb')

class Game():

    ratio = 3**0.5

    def creating_hexagon(self, x, y, a, j, i):
        position = [j, i]
        color = ['white', 'yellow', 'white', 'yellow']
        filling = color[random.randint(0,1)]
        hexa = canvas.create_polygon(x, y, x+a, y, x+a+(a/2), y+a*self.ratio/2, x+a, y+a*self.ratio, x, y+a*self.ratio, x-(a/2), y+a*self.ratio/2, outline='black', fill=filling, tags=[position, filling])
        print(position)


    def board_coord(self, n, x0, y0, a):
        emptyBoard = [['null']*n for _ in range(n)]
        for j in range(len(emptyBoard)):
            for i in range(len(emptyBoard[j])):
                p1 = x0
                p2 = y0 + j*(a*(3**0.5))
                if j <= n//2:
                    for i in range(0, n):
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        if i <= n//2+j:
                            emptyBoard[j][i] = [x, y]
                elif j > n//2:
                    for i in range(0, n):
                        x = p1 + i*(a+a/2)
                        y = p2 - i*(a*self.ratio/2)
                        if i > j-n//2-1:
                            emptyBoard[j][i] = [x, y]

        #print(emptyBoard)
        return emptyBoard

    def hive(self, n, x0, y0, a):
        for j in range(len(self.board_coord(n, x0, y0, a))):
            for i in range(len(self.board_coord(n, x0, y0, a)[j])):
                if self.board_coord(n, x0, y0, a)[j][i] != 'null' :
                    x = self.board_coord(n, x0, y0, a)[j][i][0]
                    y = self.board_coord(n, x0, y0, a)[j][i][1]
                    time.sleep(0.1)
                    self.creating_hexagon(x, y, a, j, i)
                    canvas.update()

        canvas.mainloop()

    def click(self):
        if canvas.find_withtag(CURRENT):
            print(canvas.gettags(CURRENT))
            pos = canvas.gettags(CURRENT)[0]
            tags = canvas.gettags(CURRENT)
            if 'yellow' in tags:
                canvas.itemconfig(CURRENT, fill='white')
                canvas.dtag(CURRENT, 'yellow') #deletes the yellow tag!!!
                canvas.addtag_withtag('white', CURRENT)
                print(canvas.gettags(CURRENT))
            elif 'white' in tags:
                canvas.itemconfig(CURRENT, fill='yellow')
                canvas.dtag(CURRENT, 'white')
                canvas.addtag_withtag('yellow', CURRENT)
                print(canvas.gettags(CURRENT))
            #neighbours:
            first = str(int(pos[0])-1)+" "+str(int(pos[2]))
            second = str(int(pos[0]))+" "+str(int(pos[2])-1)
            third = str(int(pos[0])-1)+" "+str(int(pos[2])-1)
            fourth = str(int(pos[0])+1)+" "+str(int(pos[2])+1)
            fifth = str(int(pos[0])+1)+" "+str(int(pos[2]))
            sixth = str(int(pos[0]))+" "+str(int(pos[2])+1)
            if 'white' in canvas.gettags(first):
                canvas.itemconfig(canvas.find_withtag(first), fill="yellow")
                canvas.dtag(canvas.find_withtag(first), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(first))
            else:
                canvas.itemconfig(canvas.find_withtag(first), fill='white')
                canvas.dtag(canvas.find_withtag(first), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(first))
            if 'white' in canvas.gettags(second):
                canvas.itemconfig(canvas.find_withtag(second), fill="yellow")
                canvas.dtag(canvas.find_withtag(second), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(second))
            else:
                canvas.itemconfig(canvas.find_withtag(second), fill='white')
                canvas.dtag(canvas.find_withtag(second), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(second))
            if 'white' in canvas.gettags(third):
                canvas.itemconfig(canvas.find_withtag(third), fill="yellow")
                canvas.dtag(canvas.find_withtag(third), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(third))
            else:
                canvas.itemconfig(canvas.find_withtag(third), fill='white')
                canvas.dtag(canvas.find_withtag(third), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(third))
            if 'white' in canvas.gettags(fourth):
                canvas.itemconfig(canvas.find_withtag(fourth), fill="yellow")
                canvas.dtag(canvas.find_withtag(fourth), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(fourth))
            else:
                canvas.itemconfig(canvas.find_withtag(fourth), fill='white')
                canvas.dtag(canvas.find_withtag(fourth), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(fourth))
            if 'white' in canvas.gettags(fifth):
                canvas.itemconfig(canvas.find_withtag(fifth), fill="yellow")
                canvas.dtag(canvas.find_withtag(fifth), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(fifth))
            else:
                canvas.itemconfig(canvas.find_withtag(fifth), fill='white')
                canvas.dtag(canvas.find_withtag(fifth), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(fifth))
            if 'white' in canvas.gettags(sixth):
                canvas.itemconfig(canvas.find_withtag(sixth), fill="yellow")
                canvas.dtag(canvas.find_withtag(sixth), 'white')
                canvas.addtag_withtag('yellow', canvas.find_withtag(sixth))
            else:
                canvas.itemconfig(canvas.find_withtag(sixth), fill='white')
                canvas.dtag(canvas.find_withtag(sixth), 'yellow')
                canvas.addtag_withtag('white', canvas.find_withtag(sixth))

            canvas.itemconfig('<Button-1>', fill="blue")
            canvas.update_idletasks()
            canvas.after(200)
            #canvas.itemconfig(CURRENT, fill="red")

    root.bind('<Button-1>', click)


game = Game()
game.hive(5, 100, 150, 50)
