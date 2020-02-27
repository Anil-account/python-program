class costomer():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def withdraw (self, amount):
        self.balance -= amount
        return self.balance
    def deposite (self, amount):
        self.balance += amount
        return self.balance
c1 = costomer("mike", 2000)
print(c1.withdraw(1000))
print(c1.deposite(1000))
c2 = costomer ("john", 9000)
print(c2.withdraw(1000))
print(c2.deposite(2000))
c1.balance = 3000
c1 = costomer("mike", 2000)
print(c1.name)
print(c1.balance)
c1.balance = 3000
print(c1.balance)