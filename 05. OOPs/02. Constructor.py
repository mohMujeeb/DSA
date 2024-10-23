# All Classes have a function called __init__, which is always executed when the object
# is being instantiated

class Animal:
    def __init__(self, name): # Constructor
        self.name = name
    
A1 = Animal("Dog")


#Types of Constructors

class Student:
    # Default Constructor
    def __init__(self):
        pass
    
    # Parameterized constructor    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
S1 = Student("John", 80)
print(S1.name, S1.marks)
