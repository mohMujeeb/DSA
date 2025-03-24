"""Problem Statement: Create a BankAccount class with the following attributes and methods:
Attributes:
    - account_holder: (string) Name of the account holder.
    - balance: (float) Balance of the account (initially set to 0.0).

Methods:
    - Getter and Setter for balance:
        - The getter method should return the current balance.
        - The setter method should set the balance. Ensure that the balance cannot be set to a negative value.
    - Deposit Method:
        - Accepts an amount to deposit into the account. Ensure that the deposit amount is positive.
    - Withdraw Method:
        - Accepts an amount to withdraw from the account. Ensure that the withdrawal does not exceed the current balance and the amount is positive.
    - Display Account Information:
        - A method to display the account holder's name and balance.
"""

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.__account_holder = account_holder
        self.__balance = max(float(balance), 0.0)
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = value
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")

        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")            
        else: 
            print("Invalid Deposit Amount!")
            
    def display_account_info(self):
        print("Account Holder: {}".format(self._BankAccount__account_holder),
              "\nBalance: ${:.2f}".format(self._BankAccount__balance))
        

# Example usage
account = BankAccount("Nova", 1000)
# Depositing money
account.deposit(500)
# Withdrawing money
account.withdraw(300)
# Display updated info
account.display_account_info()