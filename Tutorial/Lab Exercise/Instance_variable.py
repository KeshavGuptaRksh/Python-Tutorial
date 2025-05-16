class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    # Instance method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

# Create accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob")

account1.deposit(500)  # Deposited 500. New balance: 1500
account2.withdraw(100) # Insufficient funds