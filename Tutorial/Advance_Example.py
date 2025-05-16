class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    @property
    def account_holder(self):
        return self._account_holder
    
    @account_holder.setter
    def account_holder(self, value):
        if not isinstance(value, str):
            raise TypeError("Account holder must be a string")
        if len(value) < 2:
            raise ValueError("Account holder name too short")
        self._account_holder = value

account = BankAccount("Alice", 1000)
print(account.balance)        # 1000
account.balance = 1500        # Valid
# account.balance = -500      # Raises ValueError

print(account.account_holder) # Alice
account.account_holder = "Bob" # Valid
# account.account_holder = 123 # Raises TypeError