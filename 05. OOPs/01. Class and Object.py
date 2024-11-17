# Class -> A blueprint for all objects having similar attributes and behavior.

# defining class
class SmartPhone:
    # constructor
    def __init__(self, device, brand):
        self.device = device
        self.brand = brand
        
    # method of the class
    def description(self):
        return f"This is a {self.brand}'s {self.device}."
    
# creating object of class

obj = SmartPhone("S21", "Samsung")
print(obj.description())


# Employee class with employee count, name and their salaries.

class Employee:
    emp_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
        
    def display_count(self):
        return f"Total number of employees: {Employee.emp_count}"
    
    def display_employee(self):
        return f"Name: {self.name}, Salary: {self.salary}"
    
# Creating objects of Employee class
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)

print(e1.display_employee())
print(e2.display_employee())
print(e1.display_count())


# Garbage collection __del__() destructor
""" 
The process by which python periodically reclaims blocks of memory that no
longer in use is termed as Garbage Collection.
"""
class GarbageCollector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "Destroyed")

gc1 = GarbageCollector()
gc2 = gc1
gc3 = gc2

# Print the ids
print(id(gc1), id(gc2), id(gc3))

del gc1, gc2, gc3        


# Data Hiding in Python 
""" 
An object's attributes may or may not be visible outside the class definition.
"""
class DataHiding:
    __secretCount = 0
    
    def count(self):
        self.__secretCount += 1
        return self.__secretCount 
        
obj = DataHiding()

print(obj.count())  #Output -> 1
print(obj.count()) #Output -> 2
print(obj._DataHiding__secretCount) #Output -> 2