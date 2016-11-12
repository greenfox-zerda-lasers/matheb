from tkinter import *

root = Tk()
size = 600

canvas = Canvas(root, width=size, height=size, bg='yellow')
canvas.pack()

def squares(x, y, size, n):
    if n == 0:
        return
    canvas.create_line(x, y + (size/3), x + size, y + (size/3), fill = 'black')
    canvas.create_line(x, y + (2*size/3), x + size, y + (2*size/3), fill = 'black')
    canvas.create_line(x + (size/3), y, x + (size/3), y + size, fill = 'black')
    canvas.create_line(x + (2*size/3), y, x + (2*size/3), y + size, fill = 'black')

    squares(x + size/3, y, size/3, n-1)
    squares(x, y + size/3, size/3, n-1)
    squares(x + size/3, y + 2*size/3, size/3, n-1)
    squares(x + 2*size/3, y + size/3, size/3, n-1)

squares(0, 0, 600, 5)

root.mainloop()
