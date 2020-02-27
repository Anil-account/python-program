
# import random num
from tkinter import *

try:
    from tkinter import messagebox
except:
    import tkMessageBox as messagebox
root = Tk()

def ran():
    import random
    messagebox.showinfo("hello",random.randint(1,7))

# def lb():
#     lable = Label(root,fg = "Black",text = "press")
#     lable.pack()

b= Button(root,text = 'click',command = ran)


b.pack()
root.mainloop()