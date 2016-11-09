# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *
import random

def draw_star(num): #only needs, how many lines would you draw for each quarter

    root = Tk()

    w = 300
    h = 300

    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    for i in range(num+1):
        x = i * w / num
        y = i * h / num
        canvas.create_line(w, y, x, 0, fill = 'purple')
        canvas.create_line(0, y, x, h, fill = 'green')
    root.mainloop()

draw_star(10)
