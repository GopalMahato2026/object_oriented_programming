### A class is a blue print of creating object, attribute, methods
"""
class Car:
    pass
audi = Car()
bmw = Car()
audi.window = 4
print(type(audi), audi.window)
print(type(bmw), bmw)
print(dir(Car))    
"""
"""
class Dog:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
#creating object
dog1 = Dog("Rock", 12)
print(dog1)

print(dog1.name)
print(dog1.age)
"""
"""
class Dog_:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof!")
     
dog_main = Dog_("Rocky", 3)
print(dog_main)
dog_main.bark()
"""
#### Modeling a Bank Account
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposite(self, amount):
        if amount < 0:
            print(f"{amount} can't be negative")
        self.balance += amount
        print(f"{amount} deposited sucessfully!\nNew Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent Funds!")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn successfully!\nNew balance is {self.balance}")
    def get_balance(self):
        return self.balance
gopal = BankAccount("Gopal Mahato")        
gopal.deposite(400000)
gopal.withdraw(1000)
print(gopal.get_balance())





