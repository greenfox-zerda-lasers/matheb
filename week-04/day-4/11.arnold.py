from tkinter import *

root = Tk()
size = 600
canvas = Canvas(root,width=size, height=size, bg="yellow")
canvas.pack()

def nervtangle(x,y,size):
    canvas.create_rectangle(x,y,x+size,y+size)
    if size > 20:
        nervtangle(x,y+size/3,size/3)
        nervtangle(x+(size*(2/3)),y+size/3,size/3)
        nervtangle(x+size/3,y,size/3)
        nervtangle(x+size/3,y+(size*(2/3)),size/3)

nervtangle(0,0,600)

root.mainloop()
