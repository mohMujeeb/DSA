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