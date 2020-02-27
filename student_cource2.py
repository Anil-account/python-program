# # creat a class, initiate a constructor , use basic variables like, self.name, self.address, simillarly creat other function like:get marks, this inputs the value from user into a variable
# # now also creat other functions like total and avg marks, this calculates hte average and total marks based on the marks we got form other functions as of user.
# class student():
#     # this is the constructor with two default attributes like name and address , so we aspect at least two parameter from student while creating an object
#     def __init__(self, name, address):
#         self.name = name
#         self.addr = address
#         self.marks_sub = ['eng', 'nep', 'maths']
#         self.usr_marks = []
#
#     # this method prints the information of particular student
#     def print_info(self):
#         print('tour name and address is ::: ' + self.name, self.addr)
#
#     def gets_marks(self):
#
#         for i in range(len(self.marks_sub)):
#             val = input('enter no ')
#             self.usr_marks.append(int(val))
#
#     def display_avg(self):
#         total = sum(self.usr_marks)
#         avg = total / len(self.marks_sub)
#         print('our avg marks is', avg)
#
#     def find_highest_marks_sub(self):
#         a = 0
#         for i in range(len(self.usr_marks)):
#
#             if (self.usr_marks[i] == max(self.usr_marks)):
#                 a = i
#         print(self.usr_marks[a])
#         print(self.marks_sub[a])
#         return a
#
#
# x = student('subash', 'ktm')  # this is the creation of an object called x
# x.print_info()  # we are using the functions assiciated with an object type student , x
# x.gets_marks()  # we are using fnction from the student to get marks
# x.display_avg()  # WE ARE  using function from student object to display the average marks from student
# x.find_highest_marks_sub()
#
#
# class course_class():
#
#     def __init__(self, name, course):
#         self.name = name
#         self.cource = course
#         #constructuor,method
#
#
#

#
# class marks():
#     def __init__(self,name,marks):
#         self.marks = marks
#         self.name = name
#         self.m =[]
#         self.sub = ["Math","Eng","Programming"]
#
#     def detail(self):
#         print("This is result of the student",self.name)
#
#     def get_mark(self):
#         for i in range(len(self.sub)):
#             v = (input("enter mark of ",(self.sub[i])))

# a = ['a','f','g']
# for i in range(5):
#     for i in range (len(a)):
#         print(i)
#         print(a)



