### Encapsulation with Getter and Setter Methods
## Public, protected, private
"""
class Person:
    def __init__(self, name, age):
        self.name = name ## public variables
        self.age = age ## also public variables
        
def get_data(ar):
    return ar.name, ar.age
p1 = Person("Gopal", 19)
print(p1.name)
print(p1.age)
#print(dir(p1))
print(get_data(p1))
print("--------NEW TOPIC PRIVATE ATTRIBUTE---------")
## making private variables not public
class Person2:
    def __init__(self, name, age, gen):
        self.__name = name ## public variables
        self.__age = age ## also public variables
        self.gen = gen
def get_data(ar):
    return ar.__name, ar.__age, ar.gen
p2 = Person2("Gopal Mahato", 19, "Man")
print(dir(p2))
#print(get_data(p2))
print("-------NEW SECTION PROTECTED ATTRIBUTE--------")
class People:
    def __init__(self, name, age, gen):
        self._name = name ## protected variables
        self._age = age ## this is also protected variables
        self.gen = gen
class Employee(People):
    def __init__(self, name, age, gen):
        super().__init__(name, age, gen)
e1 = Employee("Gopal Mahato", 19, "Male")
print(e1._name)
"""
#Encapsulation with getter and setter method
class Person:
    def __init__(self, name, age):
        self.__name = name # private access modifier or variable
        self.__age = age ## private variable
    ### getter method for name
    def get_name(self):
        return self.__name
    ## setter method for name
    def set_name(self, name):
        self.__name = name  
    ## getter method for age
    def get_age(self):
        return self.__age
    ## setter method for age
    def set_age(self, age):
        if age < 0:
            print("age can't be negative")
        self.__age = age    
 
person = Person("Gopal", 19)
## acceses and modify private variables using getter and setter
print(person.get_name())
print(person.get_age())
person.set_name("Gopal Mahato")
print(person.get_name())
print("-------------THIS PROGRAM ENDS HERE--------------")

        






























































