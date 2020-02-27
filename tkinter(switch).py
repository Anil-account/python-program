# import tkinter as tk
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
#         self._frame.pack()
#
# class Login(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.Label(self, text ="This is the Login page").pack()
#         tk.Button(self,text = "Open Employee page",
#                  command = lambda : master.switch_frame(Employee)).pack()
#         tk.Button(self,text = "Open Department Page",
#                  command = lambda :master.switch_frame(Department)).pack()
#         tk.Button(self,text = "Open College Page",
#                   command = lambda :master.switch_frame(College)).pack()
#
# class Employee(tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.Label(self, text = "This is Employee Page").pack()
#         tk.Button(self, text = "Return to Login Page",
#                   command = lambda :master.switch_frame(Login)).pack()
#
# class Department (tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.Label(self, text = "This is Department Page").pack()
#         tk.Button(self, text = "Return to Login Page",
#                   command = lambda :master.switch_frame(Login)).pack()
#
# class College (tk.Frame):
#     def __init__(self,master):
#         tk.Frame.__init__(self,master)
#         tk.Label(self, text = "This is college Page").pack()
#         tk.Button(self, text = "Return to Login Page",
#                   command = lambda :master.switch_frame(Login)).pack()
#
# app=MainApp()
# app.mainloop()
def syn(n):
    if n <1:
        raise ValueError("error")
    elif n == 1 or n ==2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3,n+1):
            tem = a+b
            a = b
            b = tem
            return b
print(syn(5))