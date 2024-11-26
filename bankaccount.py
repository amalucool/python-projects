class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be set to a negative value.")
        self._balance = amount

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")

account = BankAccount(100)
account.deposit(50)
print(account.balance)  #
account.withdraw(30)
print(account.balance)  

try:
    account.balance = -10
except ValueError as e:
    print(e)  
