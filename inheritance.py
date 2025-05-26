"""
Inheritance is a fundamental concept in object oriented programming (OOP) that allows a class to inherit attributes and methods from another class. This lesson covers  single inheritance and multiple inheritance. demonstrating how to create and use them in python
"""
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
        
"""
"""
class Human:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age 
        self.country = country
    def show_data(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCountry: {self.country}")
    
    def personal_data(self):
        if self.age > 1 and self.age < 18:
            print("You are child!")
        if self.age > 18 and self.age < 60:
            print("You are in middle age!")
class Male(Human):
    def __init__(self, name, age, country, sex):
        super().__init__(name, age, country)
        self.sex = sex
    def male_data(self):
        if self.age > 18 and self.age < 30:
            print(f"{self.name}, You have Young energy!\nBecause You have the power to change the shape of the world!")
        if self.age > 30 and self.age < 60:
            print(f"{self.name}, You are well aged Men!")
            
        if self.age > 60:
            print(f"According to the world {self.name} You are a Old MEN You have lots of experience")
male1 = Male("Gopal", 19, "India", "male")
male1.show_data()
male1.male_data()
print("___"*4, "NEW OBJECT ON THE WAY", "---"*4)
male2 = Male("Dadu", 78, "India", "male")
male2.show_data()
male2.male_data()    
        
"""


print("This is the buttom of the program\nPrograms ends here!")

    
    
