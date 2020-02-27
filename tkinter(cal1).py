# to male calculator design
from tkinter import *
cal=Tk()
lbl = Label(cal)
lbl.grid(row = 0,column = 0)
def a():
    lbl['text'] = 1
def b():
    lbl['text'] = 2
def c():
    lbl['text'] = 3
def d():
    lbl['text'] = 4
def e():
    lbl['text'] = 5
def f():
    lbl['text'] = 6
def g():
    lbl['text'] = 7
def h():
    lbl['text'] = 8
def i():
    lbl['text'] = 9
def j():
    lbl['text'] = 0
def lab():
    label =Label(cal,fg ='green',text = "Anil Calculator")
    label.grid(row = 5,column =3)


A = Button(cal,text = '1',command = a,).grid(row = 1,column =0)
B = Button(cal,text = '2',command = b).grid(row = 1,column =1)
C = Button(cal,text = '3',command = c).grid(row = 1,column =2)
D = Button(cal,text = '4',command = d).grid(row = 2,column =0)
E = Button(cal,text = '5',command = e).grid(row = 2,column =1)
F = Button(cal,text = '6',command = f).grid(row = 2,column =2)
G = Button(cal,text = '7',command = g).grid(row = 3,column =0)
H = Button(cal,text = '8',command = h).grid(row = 3,column =1)
I = Button(cal,text = '9',command = i).grid(row = 3,column =2)
J = Button(cal,text = '0',command = j).grid(row = 4,column =0)
B2= Button(cal,text = 'HI', command = lab).grid(row = 4,column = 3)


cal.mainloop()