# Constructors 
""" 
Python constructor is an instance method in a class, that is automatically called whenever 
a new object of the class is created.

Python uses a special method called __init__ to initialize instance variable for the object as 
soon as it is declared.
"""

# Creating a Constructor in Python

""" 
def __init__(self, parameters):
Initialize the instance variables

"""


# Types of the constructors:
""" 
    -> Default constructor - does not accept any parameter other than the self
    -> Parameterized constructor
"""

# Default constructor
print("Default Constructor")
class Employee:
    # Base class for all employees
    
    def __init__(self):
        self.name = "Any"
        self.age = 19
        
objEmp = Employee()

print("Name: {}".format(objEmp.name))
print("Age: {}".format(objEmp.age))


# Parameterized constructor
print("Parameterized Constructor")
class Employee:
    # Base class for all employees
    
    def __init__(self, empID, empSalary):
        self.empID = empID
        self.empSalary = empSalary
        
objEmp = Employee(1, 20000)

print("Employee ID: {}".format(objEmp.empID))
print("Employee Salary: {}".format(objEmp.empSalary))

# How to achieve functionality similar to multiple constructors
print("Multiple Constructor Functionality")
class Employee:
    # Base class for all employees
    
    def __init__(self, *args):
        if len(args) == 1:
            self.empID = args[0]
        elif len(args) == 2:
            self.empID = args[0]
            self.empSalary = args[1]
        
mulEmp = Employee(1)
print("Employee ID: {}".format(mulEmp.empID))

mulEmp2 = Employee(1, 20000)
print("Employee ID: {}".format(mulEmp2.empID))
print("Employee Salary: {}".format(mulEmp2.empSalary))