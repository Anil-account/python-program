# to make login page
import tkinter as tk

from tkinter import messagebox

from tkinter import *

from tkinter import ttk


# creating frame


class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
        self.geometry("800x600")  # to make geomerty of frame
        self.resizable(width=False, height=False)  # to fix geometry frame

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class Login(tk.Frame):  # making a frame for login page
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master.title("Login System")  # frame title
        self.screen = tk.Frame
        tk.Label(self, text="This is Login Page", font=40, fg="blue").grid()
        tk.Label(self, text="E-mail").grid()  # creating lable
        tk.Label(self, text="Password", ).grid()
        tk.Button(self, text="Login", fg="white", bg="green",  # adding background color
                  command=self.read).grid()
        tk.Button(self, text="Sign Up", bg='sky blue', fg="white",
                  command=lambda: master.switch_frame(Account)).grid(row=3, column=1)
        # Inserting photo
        self.photo_frame = tk.Frame(self, width=15, height=20)  # increasing height and weight
        self.photo_frame.grid(row=0, column=1)
        self.logo = PhotoImage(file="logo.png")  # inserting photo in png
        self.lable = tk.Label(self.photo_frame, image=self.logo)
        self.lable.grid()
        self.e1 = tk.Entry(self, width=25)
        self.e1.grid(row=1, column=1)  # entry for E-mail
        self.e2 = tk.Entry(self, show="*", width=25)  # entry for password
        self.e2.grid(row=2, column=1)
        self.l1 = tk.Label(self)  # to show text is password sosent match
        self.l1.grid()
        self.list1 = []  # to store data if login in list

    def read(self):  # to check username and password

        file = open("login.txt", "r")  # reads data from login.txt
        data = file.readlines()
        file.close()
        for item in data:
            value = item.replace("\n", "")  # replace "\n" by none
            data2 = value.split(',')  # add "," in word
            self.list1.append(data2)  # converting into 2d matrix
        x = 0
        for i in range(len(self.list1)):
            if self.e1.get() == self.list1[i][0] and str(self.e2.get()) == self.list1[i][1]:  # checking
                # password and e-mail from list
                x = 1
                break
        if x == 1:
            self.master.switch_frame(Department1)
        elif self.e1.get() == "admin" and self.e2.get() == "admin":  # to check if he is admin or not
            self.master.switch_frame(Admin)
        else:
            messagebox.showinfo("Error", "Please enter E-mail and Password")  # to display message in messagebox


class Account(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Account")
        tk.Label(self, text="Create an account", font=13, bg="Green").grid()
        tk.Label(self, text="Sign up for Free", font="7").grid()
        tk.Label(self, text="First Name").grid()
        tk.Label(self, text="Last Name").grid(row=2, column=2)
        tk.Label(self, text="Gender").grid()
        tk.Label(self, text="E-mail").grid()
        tk.Checkbutton(self, text="male").grid(row=3, column=1)  # to add check button
        tk.Checkbutton(self, text="female").grid(row=3, column=2)
        tk.Label(self, text="Password").grid()
        tk.Label(self, text="Confirm password").grid(row=5, column=2)
        tk.Label(self, text="Month").grid(row=6, column=2)
        tk.Label(self, text="year").grid(row=6, column=0)
        tk.Label(self, text="Day", width=10).grid(row=6, column=4)
        tk.Button(self, text="Submit", font=1,
                  command=self.write).grid(row=7, column=1)
        tk.Button(self, text="Return", font=1,
                  command=lambda: self.master.switch_frame(Login)).grid(row=7, column=3)

        self.a = tk.Entry(self)  # entry for first name
        self.a.grid(row=2, column=1)
        self.b = tk.Entry(self)  # entry for last name
        self.b.grid(row=2, column=3)
        self.c = tk.Entry(self)  # entry for email
        self.c.grid(row=4, column=1)
        self.d = tk.Entry(self, show="*")  # entry password and to shows word/number to * sign
        self.d.grid(row=5, column=1)
        self.e = tk.Entry(self)  # entry for month
        self.e.grid(row=6, column=1)
        self.f = tk.Entry(self)  # entry for year
        self.f.grid(row=6, column=3)
        self.g = tk.Entry(self)  # entry for day
        self.g.grid(row=6, column=5)
        self.h = tk.Entry(self, show="*")  # to confirm password
        self.h.grid(row=5, column=3)
        self.l2 = tk.Label(self, font="Arial")
        self.l2.grid()

    def same(self):  # to check if password match or not
        if self.d.get() == self.h.get():
            self.config(command=self.write)
            self.l2.config(text="Login Created")  # if password matches display login created
        else:
            self.l2.config(text="Password doesn't't match")  # display label if doesn't match

    def write(self):  # to check if entry has been filled or not
        if self.a.index('end') == 0 or self.b.index('end') == 0 or self.c.index('end') == 0 or self.d.index(
                'end') == 0 or self.e.index('end') == 0 or self.f.index('end') == 0 or self.g.index('end') == 0:
            self.l2.config(text="Data is required")

        elif self.d.get() != self.h.get():  # to match password
            self.l2.config(text="Password doesn't match")
        else:
            file = open("login.txt", "a")  # to add data in sclected file
            res = self.c.get() + "," + self.d.get() + "," + self.a.get() + "," + self.b.get() + "\n"
            file.write(res)
            file.close()
            messagebox.showinfo("Welcome", "Account has been created")  # to display message box
            self.a.delete(0, 'end')  # to delete entries
            self.b.delete(0, 'end')
            self.c.delete(0, 'end')
            self.d.delete(0, 'end')
            self.e.delete(0, 'end')
            self.f.delete(0, 'end')
            self.g.delete(0, 'end')
            self.h.delete(0, 'end')


class Admin(tk.Frame):  # this frame is for Admin
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Admin Management System")
        tk.Label(self, text="Welcome Admin", font="Arial", width=19).grid()
        tk.Label(self, text="Department").grid()
        tk.Label(self, text="ID").grid()
        tk.Button(self, text="Save Department",  # to save department
                  command=self.save).grid(row=4, column=1)
        tk.Label(self).grid(row=3, column=0)
        tk.Label(self).grid(row=3, column=1)
        tk.Label(self, width=25).grid(row=3, column=2)
        tk.Button(self, text="log Out",  # to return to login page
                  command=lambda: master.switch_frame(Login)).grid(row=4, column=0)
        tk.Button(self, text="Add employee",  # to add employee detail
                  command=lambda: master.switch_frame(Department)).grid(row=4, column=2)
        self.e3 = tk.Entry(self)  # to add department
        self.e3.grid(row=1, column=1)
        self.e4 = tk.Entry(self)  # to add id
        self.e4.grid(row=2, column=1)
        self.lab = tk.Label(self, fg='green')  # to show text in label
        self.lab.grid()
        self.list = []  # to arrange data in list

    def save(self):
        if self.e3.index('end') == 0 or self.e4.index('end') == 0:  # if entry are blank
            self.lab.config(text="Can't create")
        else:

            file = open("department.txt", 'a')  # adds data in department
            dep = self.e3.get() + ',' + self.e4.get() + "\n"
            file.write(dep)
            file.close()
            self.lab.config(text="Department created")
        for i in range(len(self.list)):
            if self.e3.index('end') == self.list[i][0] and self.e4.index('end') == self[i][1]:
                messagebox.showinfo("Department", "Department already exist.\n Enter new department")
                # if department already exist than message box pops
                break


class Department(tk.Frame):
    # this is for Admin
    """"This is for admin. The has all the authorities  to add department,employee detail
    or to see all detail of employment working in all department"""

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Admin Management System")  # title name
        tk.Label(self, text="Employee registration form", font="arial").grid()
        tk.Label(self, text="First Name").grid()
        tk.Label(self, text=" Last Name").grid()
        tk.Label(self, text=" ID").grid()
        tk.Label(self, text=" Address").grid()
        tk.Label(self, text=" Age").grid()
        tk.Label(self, text=" Contact no.").grid()
        tk.Label(self, text=" Department Name").grid()
        tk.Button(self, text="log Out",
                  command=lambda: master.switch_frame(Login)).grid()  # goes to login page
        tk.Button(self, text="Show detail",  # shows detail of all employee
                  command=lambda: master.switch_frame(Detail), width=18, height="5").grid(row=10, column=0)
        self.screen = tk.Frame
        self.photo_frame = tk.Frame(self, width=20, height=20)
        self.photo_frame.grid(row=9, column=0)
        self.logo = PhotoImage(file="employment pic.png")  # inserting photo
        self.lab = tk.Label(self.photo_frame, image=self.logo)
        self.lab.grid()
        self.e1 = tk.Entry(self)  # Entry of First name
        self.e1.grid(row=1, column=1)
        self.e2 = tk.Entry(self)  # Entry of Last name
        self.e2.grid(row=2, column=1)
        self.e3 = tk.Entry(self)  # Entry of ID
        self.e3.grid(row=3, column=1)
        self.e4 = tk.Entry(self)  # Entry of Address
        self.e4.grid(row=4, column=1)
        self.e5 = tk.Entry(self)  # Entry of  Age
        self.e5.grid(row=5, column=1)
        self.e6 = tk.Entry(self)  # Entry of Contact no.
        self.e6.grid(row=6, column=1)
        tk.Button(self, text='save', width=18,
                  command=self.write).grid(row=8, column=1)
        tk.Label(self, text="", width=10).grid(row=8, column=2)
        tk.Button(self, text="Return",
                  command=lambda: master.switch_frame(Admin)).grid(row=8, column=3)
        self.list1 = []  # to add data in list
        self.list2 = []
        self.show = tk.Label(self)
        self.show.grid()
        file = open("department.txt", "r")  # to read department data
        data = file.readlines()
        file.close()
        for item in data:
            value = item.replace("\n", "")
            data2 = value.split(',')
            self.list1.append(data2)  # converting into 2d matrix
        for i in range(len(self.list1)):
            self.list2.append(self.list1[i][0])

        self.variable = StringVar()
        self.option = tk.OptionMenu(self, self.variable, *self.list2)  # showing option menu of department
        self.option.grid(row=7, column=1)

    def write(self):
        if self.e1.index('end') == 0 or self.e2.index('end') == 0 or self.e3.index('end') == 0 or self.e4.index(
                'end') == 0 or self.e5.index('end') == 0 or self.e6.index('end') == 0:
            self.show.config(text='Please Fill')  # to check if entry have been full filled or not
        else:
            file = open('employee.txt', 'a')  # add employee data in file.txt
            emp = self.e1.get() + "," + self.e2.get() + "," + self.e3.get() + "," + self.e4.get() + "," + self.e5.get() + "," + self.e6.get() + "," + self.variable.get() + "\n"
            file.write(emp)
            file.close()
            self.show.config(text='employee save')


def error():
    tk.messagebox.showinfo("Access Denied", "Unauthorized access")  # to show error in message box


class Department1(tk.Frame):  # This is for Employment Registration
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Employment system")
        tk.Label(self, text="Employee registration form", font="arial").grid()
        tk.Label(self, text="First Name").grid()
        tk.Label(self, text=" Last Name").grid()
        tk.Label(self, text=" ID").grid()
        tk.Label(self, text=" Address").grid()
        tk.Label(self, text=" Age").grid()
        tk.Label(self, text=" Contact no.").grid()
        tk.Label(self, text=" Department Name").grid()
        tk.Button(self, text="log Out",
                  command=lambda: master.switch_frame(Login)).grid()
        self.e1 = tk.Entry(self)  # Entry of First name
        self.e1.grid(row=1, column=1)
        self.e2 = tk.Entry(self)  # Entry of Last name
        self.e2.grid(row=2, column=1)
        self.e3 = tk.Entry(self)  # Entry of ID
        self.e3.grid(row=3, column=1)
        self.e4 = tk.Entry(self)  # Entry of Address
        self.e4.grid(row=4, column=1)
        self.e5 = tk.Entry(self)  # Entry of Age
        self.e5.grid(row=5, column=1)
        self.e6 = tk.Entry(self)  # Entry of Contact no.
        self.e6.grid(row=6, column=1)
        self.screen = tk.Frame
        self.photo_frame = tk.Frame(self, width=20, height=20)
        self.photo_frame.grid(row=9, column=0)
        self.logo = PhotoImage(file="employment pic.png")  # to add picture
        self.photo = tk.Label(self.photo_frame, image=self.logo)
        self.photo.grid()
        tk.Button(self, text='save', width=18,
                  command=self.write).grid(row=8, column=1)
        tk.Label(self, text="", width=10).grid(row=8, column=2)
        tk.Button(self, text="Show Details", width=18, height="5",
                  command=error).grid()
        self.list1 = []
        self.list2 = []
        self.lab = tk.Label(self)
        self.lab.grid()

        file = open("department.txt", "r")
        data = file.readlines()
        file.close()
        for item in data:
            value = item.replace("\n", "")
            data2 = value.split(',')
            self.list1.append(data2)
        for i in range(len(self.list1)):
            self.list2.append(self.list1[i][0])

        self.variable = StringVar()
        self.option = tk.OptionMenu(self, self.variable, *self.list2)
        self.option.grid(row=7, column=1)
 
    def write(self):  # Writing employment detail in Employment.txt
        if self.e1.index('end') == 0 or self.e2.index('end') == 0 or self.e3.index('end') == 0 or self.e4.index(
                'end') == 0 or self.e5.index('end') == 0 or self.e6.index('end') == 0:
            self.lab.config(text=" Entry Required")
        else:
            file = open('employee.txt', 'a')
            emp = self.e1.get() + ',' + self.e2.get() + ',' + self.e3.get() + ',' + self.e4.get() + ',' + self.e5.get() + ',' + self.e6.get() + ',' + self.variable.get() + '\n'
            file.write(emp)
            file.close()
            self.lab.config(text='Employee save')


class Detail(tk.Frame):  # method to create tree
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        frame_design = tk.Frame(self, width=700)  # to make width of frame
        frame_design.grid()
        tree = ttk.Treeview(frame_design)

        tree['column'] = ('one', 'two', 'three', 'four', 'five')  # column seperated
        tree.column('#0', width=80, stretch=tk.NO)
        tree.column('one', width=120, stretch=tk.NO)
        tree.column('two', width=120, stretch=tk.NO)
        tree.column('three', width=120, stretch=tk.NO)
        tree.column('four', width=120, stretch=tk.NO)
        tree.column('five', width=120, stretch=tk.NO)

        tree.heading('#0', text='ID', anchor=CENTER)
        tree.heading('one', text='Department', anchor=CENTER)
        tree.heading('two', text='First Name', anchor=CENTER)
        tree.heading('three', text='Last Name', anchor=CENTER)
        tree.heading('four', text='Address', anchor=CENTER)
        tree.heading('five', text='Contact no.', anchor=CENTER)

        # creating empty list
        idd = []
        department = []
        first_name = []
        last_name = []
        address = []
        contact_no = []
        emili_data = []

        file = open('employee.txt ', 'r')
        data = file.readlines()
        file.close()
        for item in data:
            value = item.replace("\n", "")
            data2 = value.split(",")
            emili_data.append(data2)

        for i in range(len(emili_data)):  # adding data in list
            first_name.append(emili_data[i][0])
            last_name.append(emili_data[i][1])
            idd.append(emili_data[i][2])
            address.append(emili_data[i][3])
            contact_no.append(emili_data[i][5])
            department.append(emili_data[i][6])

        for i in range(len(department)):  # to add data in table
            tree.insert("", "end", text=idd[i],
                        values=(department[i], first_name[i], last_name[i], address[i], contact_no[i]))

        tree.grid()
        tree.grid()


app = MainApp()
app.mainloop()
