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
        x = i * (w//2) / (num)
        y = i * (h//2) / (num)
        RR=("%02x"%random.randint(0,255))
        GG=("%02x"%random.randint(0,255))
        BB=("%02x"%random.randint(0,255))
        ge="#"
        color=ge+RR+GG+BB
        canvas.create_line(x, 0+(h/2), w/2, y+(h/2), fill = color)
        canvas.create_line(0+(w/2), y, x+(w/2), h/2, fill = color)
        canvas.create_line(0+(w/2), y, (w/2)-x, (h/2), fill = color)
        canvas.create_line((w/2), h-y, (w/2)+x, (h/2), fill = color)
    root.mainloop()

draw_star(10)
