# Create a class that displays the robot's messages, position, etc
from tkinter import *

class View():

    def __init__(self):
        self.root = ()
        self.w = 0
        self.h = self.w
        self.size = 10
        #self.canvas = Canvas(self.root, width=self.w, height=self.h)

    def draw_position(self, position_x, position_y, name, mood):

        self.root = Tk()
        self.w = 1000
        self.h = self.w
        self.size = 30
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.pack()

        self.canvas.create_polygon(position_x, position_y, position_x+self.size, position_y, position_x+self.size, position_y+self.size, position_x, position_y+self.size, fill='blue')

        self.canvas.create_text(25, 25, anchor = 'nw', text = "Hi, my name is "+ name + " and I feel..."+mood, tags = "text", font= 'Arial', fill='maroon')

        self.canvas.mainloop()
