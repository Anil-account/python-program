
# start up of page
# from tkinter import *
# master = Tk()
# w = Canvas(master, width = 40,height = 60)
# w.pack()
# canvas_height = 20
# canvas_width = 200
# y = int(canvas_height/2)
# w.create_line(0,y,canvas_width,y)
# mainloop()

# to make button
from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side = BOTTOM)
redbutton = Button(frame,text = 'Red',fg = 'red')
redbutton.pack(side = LEFT)
greenbutton = Button(frame,text = 'Brown',fg = 'brown')
greenbutton.pack(side = LEFT)
bluebutton = Button(frame,text = 'Blue',fg = 'blue')
bluebutton.pack(side = LEFT)
blackbutton  = Button(bottomframe,text = 'Black',fg = 'black')
blackbutton.pack(side = BOTTOM)
root.mainloop()