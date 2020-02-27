#to print button in lable
# to make calculater
from tkinter import *
cal = Tk()
Label(cal,text = 'result :').grid(row = 0)
lbl = Label(cal)

e1 = Entry(cal)
lbl.grid(row = 0,column = 1)

# e1.grid(row = 0, column = 1)
def a():
    lbl['text'] = 1
def b():
    lbl['text'] = 2
def c():
    lbl['text'] = 3
A = Button(cal,text = '1', command = a).grid(row =1,column =0)
B = Button(cal,text = '2',command = b).grid(row = 1,column = 1)
C = Button(cal,text = '3',command = c).grid(row =1,column = 2)

mainloop()