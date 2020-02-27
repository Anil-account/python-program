from tkinter import *
master =Tk()
Label(master,text='first name').grid(row=0)
Label(master,text='last name').grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
lbl = Label(master, fg="green",text="this is simple text")
lbl.grid(row=3,column=1)
def change_text():
    print("full Name = %s,\n %s" %(e1.get(),e2.get()))
    res=str(e1.get()+" "+e2.get())
    lbl['text'] = res
btn = Button(master, text='and or show',command=change_text).grid(row=2,column=1)


# btn.grid(row=2,column=1)
mainloop()