# class person():
#     def __init__(self,name,address,phone):
#         self.name = name
#         self.address = address
#         self.phone = phone
#
#     def introduce(self):
#         return"hi my name is "+self.name
#
# class Teacher (person):
#     def __init__(self,name,address,phone,subject):
#         person.__init__(self,name,address,phone)
#         self.subject = subject
#
# class Student(person):
#     def __init__(self,name,address,phone,group):
#         person.__init__(self,name,address,phone)
#         self.group = group
#
# p = person("james","KTM",123)
# print(p.name)
# print(p.introduce())
#
# t= Teacher("john","NYC",123,"python")
# print(t.name,t.subject)
# print(t.introduce())
#
#
# s = Student("sara","pokhara",123,"computing")
# print(s.name,s.group)
# print(s.introduce())


#
# class family():
#     def __init__(self,brother,age,phone):
#         self.brother = brother
#         self.age = age
#         self.phone = phone
#
#     def introduce(self):
#         return"hi your name is ", self.brother
#
# class family1(family):
#     def __init__(self,brother,age,phone,girlfriend):
#         family.__init__(self,brother,age,phone)
#         self.girlfriend = girlfriend
#
# class family2(family):
#     def __init__(self,brother,age,phone,father):
#         family.__init__(self,brother,age,phone)
#         self.father = father
#
#
# f =family("Anil",12,9877,)
# print(f.brother)
# print(f.introduce())
#
#
# f1 = family1("Bishal",18,9800,"Barsha")
# print(f1.phone,f1.girlfriend)
# print(f1.introduce())
#
#
# f2 = family2("biky",30,123,"BOI")
# print(f2.brother,f2.father)
# print(f2.introduce())


#                                                       ANIMAL LIST
# creat a class Animal, with function,
#can breath,
#can run
#can speak

#creat child class human,
# with one extra function,can think

#creat child to animal called dog
# with one extra function,is loyal

#now , using OOP, print, human can think, similarly human can breadth,run and speak and also for dog,print dog is loyal, and can breath run and speak,using concewpt of inhitirance



class Animal():
    def __init__(self,human):
        self.human = human

    def info(self):
        return(self.human +" can breath", self.human +" can run", self.human +" can speak")

class human(Animal):
    def __init__(self,human):
        Animal.__init__(self,human)

    def info1(self):
        return (self.human+ " can think")


class dog(Animal):
    def __init__(self,human):
        Animal.__init__(self,human)


    def info2(self):
        return (self.human +" is loyal")




a = Animal("bobby")
print(a.human)
print(a.info())

a1 = human("koko",)
print(a1.info1())
print(a1.info())

a2 = dog("ramesh",)

print(a2.info2())
print(a2.info())