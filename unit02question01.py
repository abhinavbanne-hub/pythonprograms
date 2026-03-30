class BankAccount:
    
    # Constructor
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    # Method to check balance
    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# ---- Main Program ----
account1 = BankAccount("123456789", 1000)

account1.check_balance()
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()
