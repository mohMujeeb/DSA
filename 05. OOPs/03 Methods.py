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
        self.name = name
        self.age = age
        Employee.empCount += 1
    
    def showcount(self):
        print(self.empCount)
        
    counter = classmethod(showcount)
    
e1 = Employee("Mujeeb", 21)
e2 = Employee("Saif", 24)

print(e1.showcount)
print()
print(Employee.counter)