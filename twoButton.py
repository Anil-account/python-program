from tkinter import *

class Gui:
    def __init__(self,root):
        self.root = root
        self.label =Label(self.root, text = "Hello World")
        self.label.pack()
        Button(self.root, text = '1',
               command = lambda : self.pressed(1)).pack(side = LEFT)
        Button(self.root, text = '2',
               command = lambda : self.pressed(2)).pack(side = LEFT)

    def pressed(self,number):
        self.label.config(text = "Pressed Button" +str(number))
root = Tk()
gui = Gui(root)
root.mainloop()