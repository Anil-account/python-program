from tkinter import *
try:
    from tkinter import messagebox
except:
    import tkMessageBox as messagebox

top = Tk()

def helloCallBack():
    messagebox.showinfo("hello python","hello world")

def showText():
    lable = Label(top,fg = "Green",text = "this is sample text")
    lable.grid()

B = Button(top,text = "hello", command = helloCallBack)
ex = Button(top,text = "Destroy Button", width = 25, command = top.destroy)
b2 = Button(top,text = "write in lable", command = showText)
B.pack()
ex.pack()
b2.pack()
top.mainloop()