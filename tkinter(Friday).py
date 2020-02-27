#
# # to make login page
#
# import tkinter as tk
# from tkinter import messagebox
#
#
# class MainApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(Login)
#
#     def switch_frame(self,frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.grid()
#
# class Login(tk.Frame):
#     def __init__(self,master):
#
#         tk.Frame.__init__(self,master,bg = "sky blue")
#         tk.Label(self,text = "This is Login Page",font = 40 ,fg = "blue",bg = "sky blue").grid()
#         tk.Label(self,text = "E-mail",bg = "sky blue").grid()
#         tk.Label(self,text = "Password",bg = "sky blue",).grid()
#         tk.Button(self,text = "Login",
#                   command = self.read).grid()
#         tk.Button(self,text = "Sign Up",
#                   command = lambda :master.switch_frame(account)).grid(row = 3,column = 1)
#
#
#
#
#         # tk.Entry(self)
#         # e2 = tk.Entry(master)
#         # e1 = tk.Entry(master)
#         # e2.grid(row=2,column=3)
#         # e1.grid(row=1,column=3)
#
#         self.e1 =tk.Entry(self)
#         self.e1.grid(row = 1,column = 1)
#         self.e2 = tk.Entry(self,show = "*")
#         self.e2.grid(row = 2,column = 1)
#
#         self.l1 = tk.Label(self,bg = "sky blue")
#         self.l1.grid()
#
#         self.list1 = []
#
#     def read(self):
#
#         file = open("login.txt","r")
#         data = file.readlines()
#         file.close()
#         for item in data:
#             value = item.replace("\n","")
#             data2 = value.split(',')
#             self.list1.append(data2)
#
#         a = 0
#
#         for i in range(len(self.list1)):
#             if self.e1.get() ==self.list1[i][0] and str(self.e2.get()) ==self.list1[i][1]:
#                 a =1
#
#             if a==1:
#                 self.master.switch_frame(page)
#                 break
#
#             # elif self.e1.index('end') ==0 or self.e2.index('get')==0:
#             #     self.l1.config(text="FILL UP",fg = 'green')
#
#             else:
#                  self.l1.config(text = "Invalid Entry")
#                  messagebox.askyesno("Error","Invalid entry")
#
#
#
#
#
# class page(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master,bg = "sky blue")
#         tk.Label(self,text = "Create Department",font = "Arial",width = 39).grid()
#         tk.Button(self, text="log Out",
#                   command=lambda: master.switch_frame(Login)).grid()
#         tk.Button(self,text = "Show E-mail and Password" )
#         # self.e3 = tk.Entry(self)
#         # self.e3.grid(row = 3 ,column = 3)
#
#
# class account(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master,bg = "sky blue")
#         # tk.Frame(self,background = "blue",height = "50",width= "50")
#         tk.Label(self,text = "Creat an account",font = 13,bg = "Green").grid()
#         tk.Label(self,text = "Sign up for Free",font = "7",bg = "sky blue").grid()
#         tk.Label(self,text = "First Name",bg = "sky blue").grid()
#         tk.Label(self,text ="Last Name",bg = "sky blue").grid(row = 2,column = 2)
#         tk.Label(self,text = "Gender",bg = "sky blue").grid()
#         tk.Label(self, text="E-mail",bg = "sky blue").grid()
#         tk.Checkbutton(self,text = "male",bg = "sky blue").grid(row = 3,column = 1)
#         tk.Checkbutton(self,text = "female",bg = "sky blue").grid(row = 3,column = 2)
#         tk.Label(self, text="Confirm password",bg = "sky blue").grid()
#         tk.Label(self,text = "Month",bg = "sky blue").grid(row = 6,column = 2)
#         tk.Label(self, text="year",bg = "sky blue").grid(row = 6,column = 0)
#         tk.Label(self, text="Day",width = 10,bg = "sky blue").grid(row = 6,column = 4)
#
#         # tk.Button(self, text="Confirm", font=1,
#         #           command=lambda: master.switch_frame(Conform)).grid(row=7, column=4)
#
#         tk.Button(self, text="Save File", font=1,
#                    command=self.write).grid(row=7, column=1)
#         tk.Button(self, text="Return to Login page", font=1,
#                    command= lambda :self.master.switch_frame(Login)).grid(row=8, column=1)
#         self.a =tk.Entry(self)
#         self.a.grid(row = 2,column = 1)
#         self.b = tk.Entry(self)
#         self.b.grid(row = 2,column = 3)
#         self.c = tk.Entry(self)
#         self.c.grid(row = 4,column =1)
#         self.d = tk.Entry(self)
#         self.d.grid(row =5,column =1)
#         self.e = tk.Entry(self)
#         self.e.grid(row = 6,column = 1)
#         self.f = tk.Entry(self)
#         self.f.grid(row = 6,column = 3)
#         # self.g = tk.Entry(self)
#         self.g = tk.Entry(self)
#         self.g.grid(row = 6,column = 5)
#         self.l2 = tk.Label(self,font = "Arial",bg = "sky blue")
#         self.l2.grid()
#
#
#
#
#     def write(self):
#
#         if self.a.index('end') == 0 or self.b.index('end') == 0 or self.c.index('end') == 0 or self.d.index('end') == 0 or self.e.index('end')==0 or self.f.index('end') == 0 or self.g.index('end')==0:
#             self.l2.config(text = "Entry is required")
#
#         else:
#             file = open("login.txt", "a")
#             res = self.c.get() + "," + self.d.get() + "," + self.a.get() + "," + self.b.get() + "\n"
#             file.write(res)
#             file.close()
#
#
# class succes(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.messagebox.showinfo("New Account","Your account has been created."+"\n"+"Please Restart the Page")
#
#         tk.Frame.__init__(self,master)
#
#
#
#
# class Conform(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.Button(self,text = "Confirm",font = 4,fg = "light grey",bg = "red",width = 13,
#                   command = lambda :master.switch_frame(succes)).grid()
#
#
#         # tk.Button(self, text="Return", font=4,
#         #           command=lambda: master.switch_frame(Login)).grid(row=1, column=0)
#
#
# app=MainApp()
# app.mainloop()
#




# The Golden Ratio is a number that appears throughout the natural world. A sequence of approximations to it is given by Gn where
# G1 = 1, and Gn = 1 + (1/Gn−1) for n > 1. Hence G2 = 1 + (1/G1) = 1 + 1 = 2 and G3 = 1 + (1/G2) = 1 + 1 2 = 3 2. (a) (15)
# Write a Python function which takes as input a positive integer and returnsasoutputthecorrespondingentryintheabovesequenceof approximations to the Golden Ratio.
# Your function should produce an appropriate error message if a negative integer is given.


i = 1
while i<=5:
    print(i)
print("Time Up!")
i = i + 1