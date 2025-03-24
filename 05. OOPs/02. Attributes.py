# Class Attributes
"""
Class Attributes are those variables that belong to a class and whose value
is shared among all ths instances of that class. It remains the same for every
instance of the class
"""

class Employee:
    #class attributes
    empCount = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        # modifying class attribute
        Employee.empCount += 1
        
        # accessing class attribute
        print("Name: ", self.__name, "Age: ", self.__age)
        print("Total Employee: ", Employee.empCount, "\n")
        
    
# Object 
e1 = Employee("Mujeeb", 21)
print()
e2 = Employee("Saif", 24)


# Instance Attribute

""" 
Instance Attribute is a variable that is specific to an individual object of class
It is defined inside the __init__() method
"""

class Person:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
        
        print("Name:", self.__name, "Age:", self.__age)
        
# object
p1 = Person("John", 25)
print()
p2 = Person("David", 30)