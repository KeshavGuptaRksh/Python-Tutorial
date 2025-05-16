class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Bank Transfer"

def checkout(processor: PaymentProcessor, amount):
    print(processor.process_payment(amount))

# Using different payment processors polymorphically
payment_methods = [
    CreditCardProcessor(),
    PayPalProcessor(),
    BankTransferProcessor()
]

for method in payment_methods:
    checkout(method, 100)
    
# Output:
# Processing $100 via Credit Card
# Processing $100 via PayPal
# Processing $100 via Bank Transfer