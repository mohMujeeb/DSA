# Class:
#   -> Attributes (Properties)
#   -> Methods (Functionality) what they can do 

class Student:
    college_name = "Islamia University Of Bahawalpur"
    
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):  # -> Method
        return f"Welcome, {self.name} to {self.college_name}!"
    
    def get_marks(self): # -> Method
        return self.marks
    
s1 = Student("Raji", 97)
print(s1.welcome())