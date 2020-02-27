from tkinter import *

window = Tk()
window.title("Wellcome to my Server")
window.geometry('400x200')
window.configure(background = "Light green")
name = Label(window,text = "Full Name").pack()
no =Label(window,text = "contact Name").pack()
lbl = Label(window,text = "empty")
lbl.pack(expand = True, fill =BOTH)

frame = Frame(window,bg ="red")
frame.pack()
name_entry =Entry(frame)
name_entry.pack()
no_entry = Entry(frame)
no_entry.pack()

def btn_click():
    res = "Welcome "+ name_entry.get()+" your no is "+ no_entry.get()
    lbl.configure(text = res)

def write():
    file = open("form.txt","a")
    res ="Wellcome "+name_entry.get() +"your no is "+no_entry.get()+"\n"
    file.write(res)
    file.close()

def read():
    file = open("form.txt","r")
    x = file.readline()
    lbl.configure(text = x)


btn = Button(window,text = "submit",command = btn_click)
rbtn = Button(window,text = "read",command = read)
wbtn = Button(window,text = "write",command = write)
btn.pack(expand = True, fill = BOTH)
rbtn.pack(expand = True, fill = BOTH)
wbtn.pack(expand = True, fill = BOTH)
window.mainloop()