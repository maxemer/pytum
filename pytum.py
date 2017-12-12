"""
PyTum Game
from EPR-Job No.5
"""
#import nadda
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"



from tkinter import * #nogo, must be edited
import tkinter as Tkinter
root = Tk()
root.title('PAvvsH TUM')
w = 550
h = 300
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def pressed(i):
    return i
    if start.zerozero.get() == 1:
        start.b.config(bg="red")
    elif zerozero.get() == 0:
        b.config(bg="lightgrey")
def start():
    but_list = []
    #win = Tkinter.Tk()
    dc_value = {}
    field_row = 1
    field_col = 1
    hure = 1
    while field_row <= 7:
        while field_col <= 7:
            #i = str(y) + str(x)
            b = Checkbutton(root, height = 2, width = 3,
                            command = lambda i = (field_row, field_col):
            print(pressed(i))).grid(row = field_row, column = field_col)
            dc_value.update({(field_row, field_col): 'em'})
            hure += 1
            field_col += 1
            but_list.append(b)

        field_col = 1
        field_row += 1
    print(dc_value)
start()
mainloop()
