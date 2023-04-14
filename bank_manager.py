from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    @abstractmethod
    def withdraw(self, amount):
        pass

class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            if self.balance < 100:
                self.balance -= 10
                print("Service charge of $10 applied for falling below minimum balance.")

class BusinessAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            if self.balance < 0:
                self.balance -= 50
                print("Service charge of $50 applied for overdraft.")
# create an instance of each account type
checking = CheckingAccount(500)
savings = SavingsAccount(1000)
business = BusinessAccount(2000)

# make some deposits and withdrawals
checking.deposit(100)
checking.withdraw(50)

savings.deposit(200)
savings.withdraw(300)

business.deposit(500)
business.withdraw(2500)

# print final balances
print(f"Checking balance: {checking.balance}")
print(f"Savings balance: {savings.balance}")
print(f"Business balance: {business.balance}")
