# # creat a class, initiate a constructor , use basic variables like, self.name, self.address, simillarly creat other function like:get marks, this inputs the value from user into a variable
# # now also creat other functions like total and avg marks, this calculates hte average and total marks based on the marks we got form other functions as of user.
# class student():
#     #this is the constructor with two default attributes like name and address , so we aspect at least two parameter from student while creating an object
#     def __init__(self,name,address):
#         self.name = name
#         self.addr = address
#         self.marks_sub = ['eng','nep','maths']
#         self.usr_marks = []
#
#     #this method prints the information of particular student
#     def print_info(self):
#         print('tour name and address is ::: '+self.name,self.addr)
#
#
#
#     def gets_marks(self):
#
#
#         for i in range(len(self.marks_sub)):
#             val = input('enter no ')
#             self.usr_marks.append(int(val))
#
#     def display_avg(self):
#         total = sum(self.usr_marks)
#         avg = total/len(self.marks_sub)
#         print('our avg marks is',avg)
#
#     def find_highest_marks_sub(self):
#         a=0
#         for i in range(len(self.usr_marks)):
#
#             if (self.usr_marks[i] == max(self.usr_marks)):
#                 a = i
#         print(self.usr_marks[a])
#         print(self.marks_sub[a])
#         return a
#
#
# x = student("Anil","KTM")
# x.print_info()
# x.gets_marks()
# x.display_avg()
# x.find_highest_marks_sub()



class course_class():

    def __init__(self,courcecredit,coursenme):
        self.Courcecreditid = courcecredit
        self.courseName = coursenme
        self.mark = 0

    def set_marks(self,marks):
        self.marks = marks

    def get_cource_detail(self):
        print('our corse info ',self.courseName , self.Courcecreditid)

    def student_name(self):
        print("student and cource")


x = course_class(9001,"Math")
x.get_cource_detail()
x.student_name()

# HIGHLY CLASSIFIED
