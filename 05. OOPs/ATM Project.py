class ATM:

    """Constructor to initialize the ATM-
       Constructor is a special method that is called when an object is created-
       Real world scenario - when user open an application, constructor is called automatically -
       Constructor is special method on which user have no control - all the functionalities in the constructor are pre-defined -
       and run automatically when user open an application"""
    def __init__(self):

        """Instance Varibales-
        A variable whose value is different for each object is called instance variable -"""

        """Access Modifiers in Python-
        1. Public - accessible from anywhere in the code -
        2. Private - accessible only within the class - denoted by double underscore (__)
        3. Protected - accessible within the class and its subclasses - denoted by single underscore (_)"""
        self.__pin = "1234"
        self.__balance = 0.0


        """When we use __ double underscore, python change that variable name to _ClassName__VariableName -
        for example - __pin will be changed to _ATM__pin - and __balance will be changed to _ATM__balance -
        So, we can access these variables using _ClassName__VariableName - which are made private -"""
        self.__menu()
    
    def __menu(self):
        user_input = input("""
        Welcome to the ATM!
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)

        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else:
            print("Exiting ATM")

    """Method to create pin"""
    def create_pin(self):
        self.__pin = input("Enter a 4 digit pin: ")
        if len(self.__pin) == 4 and self.__pin.isdigit():
            print("Pin set successffully!")
        else:
            print("Invalid pin! Please enter a 4 digit number.")
            self.create_pin() 

    """Method to deposit money"""
    def deposit(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.__pin:
            print("Pin verified successfully!")
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.__balance += amount
                print(f"Deposited: {amount}")
            else:
                print("Invalid deposit amount!")
        else:
            print("Incorrect pin!")
            self.deposit()   

    """Method to withdraw money"""
    def withdraw(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.__pin:
            print("Pin verified successfully!")
            amount = float(input("Enter amount to withdraw: "))
            if amount < self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect pin!")
            self.withdraw()
    
    """Method to check balance"""
    def check_balance(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.__pin:
            print("Pin verified successfully!")
            print(f"Your balance is: {self.__balance}")
        else:
            print("Incorrect pin!")
            self.check_balance()
        
meezan = ATM()
meezan.check_balance()