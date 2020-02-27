from tkinter import *
root=Tk()
frame=Frame(root)           #creating frame1
frame.pack()
bottomframe=Frame(root)     #creating frame2
bottomframe.pack(side=BOTTOM)       #side of 2nd frame is bottom
redbutton=Button(frame,text='Red',fg='red')
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text='Brown',fg='brown')
greenbutton.pack(side=RIGHT)
bluebutton=Button(bottomframe,text='Blue',fg='blue')
bluebutton.pack(side=RIGHT)
blackbutton=Button(bottomframe,text='Black',fg='black')
blackbutton.pack(side=LEFT)
root.mainloop()