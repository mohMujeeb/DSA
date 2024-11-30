# Three python methods categories:
"""
    1) Class Method - bound to class, not to the instance of the class
    2) Static Method - can be called on class but do not have access to cls
    parameter therefore it can not modify the class state
    3) Instance Method - can access the instance variables, can also access
    the class variables as it is common to all the objects
    
    
"""

# Class Method

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




        