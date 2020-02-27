#create class called calculation and creat a method and implement polymorphism in method where 2 or 3 parameter can be passed
class add():
    def __init__(self,a,b):
        self.b = b
        self.a = a


    def info(self):
        return (self.a + self.b)

class add1(add):
    def __init__(self,a,b,c=0):
        add.__init__(self,a,b)
        self.c = c



    def info(self):
        return("the sum is", self.a+self.b+self.c)


x = add1(2,4,1)
print(x.info())


# def add(a,b,c):
#     sum = a+b+c
#     return(sum)
#
#
# print(add(2,3,4))