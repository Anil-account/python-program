# to print sum
from tkinter import *
root = Tk()

# def ad():
#     a = int(input('enter a num'))
#     b = int(input('enter a num '))
Label(root,text = ' enter a num',).grid(row = 0)
Label(root,text = 'enter a num').grid(row = 1)
e1 =Entry(root)
e2 = Entry(root)
lbl = Label(root)
lbl.grid(row = 3, column =1)

e1.grid(row=0,column = 1)
e2.grid(row = 1,column = 1)

def add():
    e3 = int(e1.get())+int(e2.get())
    lbl['text']= e3

x = Button(root,text = "add",command = add).grid(row=3,column =0)

root.mainloop()

