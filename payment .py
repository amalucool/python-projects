class Payment:
    def __init__(self, balance, deduction):
        self.balance = balance
        self.deduction = deduction
        pass

class Paypal(Payment):
    pass

class Creditcard(Payment):
    pass

Paypal1 = Paypal("1000", "300")
Credicard1 = Creditcard("20000", "10000")

for x in (Paypal1, Credicard1):
    print(f"Your pending balance is", x.balance, "and amount to be deducted is", x.deduction)
