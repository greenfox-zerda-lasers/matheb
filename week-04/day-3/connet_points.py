# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

from tkinter import *
def connect_points(lista, listb):

    root = Tk()

    w = 300
    h = 300
    canvas = Canvas(root, width=w, height=h)
    canvas.pack()

    for k in range(len(lista)-1):
        canvas.create_line(lista[k][0], lista[k][1], lista[k+1][0], lista[k+1][1], fill='green')
    canvas.create_line(lista[k+1][0], lista[k+1][1], lista[0][0], lista[0][1], fill='green')

    for i in range(len(listb)-1):
        #for j in range(len(listb)):
        canvas.create_line(listb[i][0], listb[i][1], listb[i+1][0], listb[i+1][1], fill='green')

    root.mainloop()

lista = [[10, 10], [290,  10], [290, 290], [10, 290]]
listb = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

connect_points(lista, listb)
