class person():
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone

    def introduce(self):
        return "Hi! my name is"+ self.name

class Teacher(person):
    def __init__(self,name,address,phone,subject):
        person.__init__(self,name,address,phone)
        self.subject = subject

    def introduce(self):
        return "hi my name is "+self.name+". I am a teacher "


t= Teacher("subash","Ktm",123,"Python")
print(t.name,t.subject)
print(t.introduce())