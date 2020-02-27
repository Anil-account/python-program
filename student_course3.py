# class first():
#     # def __init(self,name):
#     #     self.cname = name
#
#     def class1(self):
#         print("this is first class")
#
#     def class2(self):
#         a = input("enter a value")
#         print("this is the first class returned to", a)
#
#     def datetoday(self):
#         print(c2.currentdate())
#
# class second():
#
#     def currentdate(self):
#         a = "sombar,mangshir 2076"
#         return a
#
# c2 = second()
# c1 = first()
# c1.class1()
# c1.class2()
# c1.datetoday()

class first():
    def __init__(self,cname):
        self.cname = cname

    def returnName(self):
        return"name of class is first "

    def returnCostomName(self):
        return"name of claas set by user is :::"+self.cname
    def getDateFromOtherClass(self):
        obj = second()
        val = obj.getDate()
        return"date returned from first class second object is :::"+val
class second():
    def __init__(self):
        self.val =""
    def getDate(self):
        return"today date is mangshir 23 2017"

first = first('jpt')
print(first.returnName())
print(first.returnCostomName())
print(first.getDateFromOtherClass())
