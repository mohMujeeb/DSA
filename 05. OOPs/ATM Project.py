class ATM:

    """Constructor to initialize the ATM-
       Constructor is a special method that is called when an object is created-
       Real world scenario - when user open an application, constructor is called automatically -
       Constructor is special method on which user have no control - all the functionalities in the constructor are pre-defined -
       and run automatically when user open an application"""
    def __init__(self):
        self.pin = ""
        self.balance = 0.0

        self.menu()
    
    def menu(self):
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
        self.pin = input("Enter a 4 digit pin: ")
        if len(self.pin) == 4 and self.pin.isdigit():
            print("Pin set successffully!")
        else:
            print("Invalid pin! Please enter a 4 digit number.")
            self.create_pin() 

    """Method to deposit money"""
    def deposit(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.pin:
            print("Pin verified successfully!")
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposited: {amount}")
            else:
                print("Invalid deposit amount!")
        else:
            print("Incorrect pin!")
            self.deposit()   

    """Method to withdraw money"""
    def withdraw(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.pin:
            print("Pin verified successfully!")
            amount = float(input("Enter amount to withdraw: "))
            if amount < self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect pin!")
            self.withdraw()
    
    """Method to check balance"""
    def check_balance(self):
        check_pin = input("Enter pin: ")
        if check_pin == self.pin:
            print("Pin verified successfully!")
            print(f"Your balance is: {self.balance}")
        else:
            print("Incorrect pin!")
            self.check_balance()
        
meezan = ATM()
meezan.check_balance()