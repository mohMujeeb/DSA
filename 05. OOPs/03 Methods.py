# Three python methods categories:
"""
    1) Class Method - bound to class, not to the instance of the class
    2) Static Method - can be called on class but do not have access to cls
    parameter therefore it can not modify the class state
    3) Instance Method - can access the instance variables, can also access
    the class variables as it is common to all the objects
    
    
"""

# Class Method using classmethod() function

class Employee:
    empCount = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
    def show_count(self):
        return self.empCount
    #Syntax -> classmethod(instance_method)
    counter = classmethod(show_count)
    
e1 = Employee("Mujeeb", 21)
print("Employee Count: ",Employee.counter())


# @classmethod

class Student:
    stdCount = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1
    
    @classmethod
    def show_count(cls):
        return cls.stdCount
    
    @classmethod
    def new_std(cls, name, age):
        return cls(name, age)
    
e1 = Student("John", 19)
s2 = Student.new_std("Mujeeb", 21)
print("Student Count: ",Student.show_count())   

# Static Method using staticmethod() function 
""" 
    - does not require any instance to be called
    - similar to class method but difference is that it does not have any
    mandatory argument like reference to object - self and reference to 
    class - cls
"""

class Car:
    carCount = 0
    def __init__(self, name, model):
        self.__name = name
        self.__model = model
        Car.carCount += 1
    # Creating a static method
    def show_count():
        return Car.carCount
    
    carCounter = staticmethod(show_count)
    
c1 = Car("Toyota", "Camry")
print("Car Count: ",Car.carCounter())


# @staticmethod

class Animal:
    animalCount = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Animal.animalCount += 1
        
    @staticmethod
    def show_count():
        return Animal.animalCount
    
ani = Animal("Elephant", 3)
print("Animal count", Animal.show_count())