class A():
    def __init__(self,name, address,id):
        self.name = name
        self._address = address #protected access in next class
        self.__id = id #privatte not access



class B(A):
    def __init__(self,name,address,id,subject):
        A.__init__(self,name,address,id)
        self.sub = subject

    def info(self):
        print(self.__id)
        self.__id = 123
        print(self.__id)


    def protected(self):
        print(self._address)


class C(B):
    def __init__(self,name,address,id,subject,day):
        B.__init__(self,name,address,id,subject)
        self.day = day

    def protected(self):
        print( "the id is ",self._address)

c = C("Anil", "Koteshwor",19022,"python","monday")
# print(C.info())
c.protected()
c.info()