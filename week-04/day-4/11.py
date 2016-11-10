from tkinter import *

root = Tk()
w = 600
h = w
canvas = Canvas(root, width=w, height=h, bg='yellow')
canvas.pack()

x = 0
y = 0

def squares(w, h, n):
    if n > 2:
        #vertical lines
        canvas.create_line(x + (w/3)*n, y, x + (w/3)*n, h, fill='black')
        canvas.create_line(x + (2*w/3)*n, y, x + (2*w/3)*n, h, fill='black')

        #horizontal lines
        canvas.create_line(x, y+(h/3)*n, w, y+(h/3)*n, fill='black')
        canvas.create_line(x, y+(2*h/3)*n, w, y+(2*h/3)*n, fill='black')
        
        squares(w/3, h, n-1)
        squares(2*w/3, h, n-1)
        squares(w, h/3, n-1)
        squares(w, 2*h/3, n-1)


root.mainloop()

squares(600, 600, 5)
