### polymorphism == multiple form
#### base class
"""
class Animal:
    def speak(self):
        return "Sound of the animal"

#derived class 1
class Dog(Animal):
    def speak(self):
        return "woof!"
        
#derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"
# functions that demonstrate polymorphism
def animal_speak(animal):
    print(animal.speak())



dog = Dog()
print(dog.speak())
cat = Cat()
print(cat.speak())
animal_speak(dog)
animal_speak(cat)
"""
# polymorphism with function and methods
# base class 1
"""
class Shape:
    def area(self):
        return "The area of the figure"
#derived class 2
class Rac_(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
#derived class 2
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14*(self.r*self.r)
#function that demonstrate polymorphism
def print_area(shape):
    print(f"The area: {shape.area()}")
rac = Rac_(10, 5)
circle = Circle(3)
print_area(rac)
print_area(circle)
"""
### Polymorphism with abstract Base class
"""
ABCs are used to define common methods for a group of related objects. They can enforce that derived classes implement particular methods, promoting consistency across different implementations.
"""
"""

from abc import ABC, abstractmethod
##difine an abstract class
class Vehicales(ABC):
    @abstractmethod
    def start_engin(self):
        pass
# derived class 1
class Car(Vehicales):
    def start_engin(self):
        return "Car engin started"
# derived class 2
class Motor_cycle(Vehicales):
    def start_engin(self):
        return "Motorcycle engin started"
## function that demonstrate polymorphism
def start_vehicales(type):
    print(type.start_engin())

car = Car()
motor_cycle = Motor_cycle()
start_vehicales(car)
start_vehicales(motor_cycle)

"""
