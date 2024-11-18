# Class Attributes
"""
Class Attributes are those variables that belong to a class and whose value
is shared among all ths instances of that class. It remains the same for every
instance of the class
"""

class Student:
    name = "kuch-bi"
    age = 10
    
obj = Student()
print("Name:", obj.name,"Age:", obj.age)