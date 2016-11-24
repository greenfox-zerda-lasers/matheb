from tkinter import *
from PIL import ImageTk, Image

class DisplayBoard():

    def __init__(self):
        self.root = Tk()
        self.w = 800
        self.h = 660
        self.tileSize = 60
        self.canvas = Canvas(self.root, width=self.w, height=self.h, bg='white')
        self.canvas.pack()
        self.floor = self.resizeImage("floor.png")
        self.wall = self.resizeImage("wall.png")
        self.hero_down = self.resizeImage("hero-down.png")
        self.hero_up = self.resizeImage("hero-up.png")
        self.hero_left = self.resizeImage("hero-left.png")
        self.hero_right = self.resizeImage("hero-right.png")
        self.monster = self.resizeImage("skeleton.png")
        self.boss = self.resizeImage("boss.png")

    def drawLevel(self, level):
        self.canvas.create_text(200, 200, anchor = 'nw', text = "Level "+ str(level), tags = "text", font= 'Arial', fill='black')

    def drawMap(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'f':
                    self.canvas.create_image(j*self.tileSize, i*self.tileSize, image=self.floor, anchor=NW)
                else:
                    self.canvas.create_image(j*self.tileSize, i*self.tileSize, image=self.wall, anchor=NW)
        self.canvas.update()

    def drawTextHero(self, HP, DP, SP, level):
        self.canvas.create_text(10*self.tileSize+10, 60, anchor = 'nw', text = "TKWanderer Game\n", tags = "text", font= 'Arial', fill='black')
        self.canvas.create_text(10*self.tileSize+10, 100, anchor = 'nw', text = "Level: "+ str(level), tags = "text", font= ('Arial', 30), fill='red')
        self.canvas.create_image(10*self.tileSize+10, 180, image=self.hero_down, anchor=NW)
        self.canvas.create_text(10*self.tileSize+10, 4*60, anchor = 'nw', text = " HP: " + str(HP) + "\n DP: " + str(DP) + "\n SP: " + str(SP) +"\n", tags = "text", font= ('Arial', 20), fill='black')

    def drawTextEnemy(self, HP, DP, SP):
        self.canvas.create_image(10*self.tileSize+10, 360, image=self.monster, anchor=NW)
        self.canvas.create_text(10*self.tileSize+10, 7*60, anchor = 'nw', text = " HP: " + str(HP) + "\n DP: " + str(DP) + "\n SP: " + str(SP) +" \n", tags = "text", font= ('Arial', 20), fill='black')

    def resizeImage(self, file_name):
        image = Image.open(file_name)
        resized_image = image.resize((self.tileSize, self.tileSize), Image.ANTIALIAS)
        return ImageTk.PhotoImage(resized_image)

    def drawCharacter(self, pos, charType):
        if charType == 'hero_down':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.hero_down, anchor=NW)
        elif charType == 'hero_up':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.hero_up, anchor=NW)
        elif charType == 'hero_left':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.hero_left, anchor=NW)
        elif charType == 'hero_right':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.hero_right, anchor=NW)
        elif charType == 'monster':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.monster, anchor=NW)
        elif charType == 'boss':
            self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.boss, anchor=NW)

    def clearCharacter(self, pos):
        self.canvas.create_image(pos[1]*self.tileSize, pos[0]*self.tileSize, image=self.floor, anchor=NW)

    def clearText(self):
        self.canvas.create_rectangle(10*self.tileSize, 0, self.w, self.h, fill="white", outline="white")

    def clearTextEnemy(self):
        self.canvas.create_rectangle(10*self.tileSize, 4*60, self.w, self.h, fill="white", outline="white")

    def clearScreen(self):
        self.canvas.create_rectangle(0, 0, self.w, self.h, fill="white", outline="white")

    def drawTextGameOver(self):
        self.canvas.create_text(100, 100, anchor = 'nw', text = "GAME\nOVER", tags = "text", font= ('Arial', 100), fill='red')
