# Access Modifiers in Python 
"""Used to restrict access to class members from outside the class"""

# Public member, protected member, and private member

class Modifiers:
    def __init__(self, name, age, salary):
        self.name = name # public variable
        self._age = age  # protected variable
        self.__salary = salary  # private variable
        
    def displayEmployee(self):
        print("Name: {}", self.name,
              "Age: {}", self._age,
              "Salary: {}", self.__salary
            )
    
mod = Modifiers("John", 18, 20000)
# print the public members
print(mod.name) 
print(mod._age) 

# to access private member outside the class we will use name mangling technique
print(mod._Modifiers__salary)


# Getter and setter methods

class GetterSetter:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    
gs=GetterSetter("Bhavana", 24)
print ("Name:", gs.get_name(), "age:", gs.get_age())
gs.set_name("Archana")
gs.set_age(21)
print ("Name:", gs.get_name(), "age:", gs.get_age())


# Property object in python 

class Property:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
        
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    
    name = property(get_name, set_name, "Name")
    age = property(get_age, set_age, "Age")
    
    
pro = Property("Lana", "19")
print("Name:", pro.name, "age:", pro.age)

pro.name = "Rachel"
pro.age = 20
print("Name:", pro.name, "age:", pro.age)