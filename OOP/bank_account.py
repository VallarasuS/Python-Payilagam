# Class = Blue Print
# Organizing functions and data
class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, x, y):
        return x - y


calc = Calculator()
total = calc.add(10,20)
difference = calc.sub(10, 5)

print(total)
print(difference)


# Bank Account blue print
class BankAccount:
    
    # double under / dunder method
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

# Object, instance
# construction, initialization
my_account = BankAccount("John", "ABC1100", 1000)
my_account.deposit(100)
my_account.withdraw(200)

another_account = BankAccount("Dave", "ABC2211", 2000)
another_account.deposit(500)
another_account.withdraw(300)

numbers = [1,2,3]
numbers.append(4)
numbers.clear()

my_account.deposit(100)
my_account.withdraw(200)