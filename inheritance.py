"""
Inheritance is a fundamental concept in object oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This lesson covers  single inheritance and multiple inheritance. demonstrating how to create and use them in python
"""
class Car:
    def __init__(self, windows, doors, engintype):
        self.windows = windows
        self.doors = doors
        self.engintype = engintype
    def drive(self): 
        print(f"The Person will drive the {self.engintype} car")
car = Car(4, 5, "petrol")
car.drive()
#### single inheritance
class Tesla(Car):
    def __init__(self, windows, doors, engintype, is_selfdriving):
        super().__init__(windows, doors, engintype) ## i am trying to calling parent class 
        self.is_selfdriving = is_selfdriving
    def self_driving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")
tesla_v1 = Tesla(4, 5, "Electric", True)
tesla_v1.self_driving()

#### multiple inheritance 
### When a class inherits from more than one base class
## base class 1
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Subclass must implement this method")


### base class 2
class Pat:
    def __init__(self, owner):
        self.owner = owner


### Derived class
class Dog(Animal, Pat):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pat.__init__(self, owner)
    def speak(self):
        return f"{self.name} say woof!"
dog_v1 = Dog("Buddy", "Gopal")
print(dog_v1.speak())
print("Owner is:", dog_v1.owner)
        
    
    
    
