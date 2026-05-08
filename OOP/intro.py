
class Car:
    
    def start():
        pass

    def stop():
        pass

    def drive():
        pass


class BankAccount:
    
    balance = 100

    def deposit():
        pass

    def withdraw():
        pass

    def transfer():
        pass

    def close():
        pass



# OOP
# class

# class - blue print
# object - manifestation of blue print

# BankAccount, 
# Bank
# Students
# Employees

class Employee:

    def __init__(self, id, name, email = ""):
        self.id = id
        self.name = name
        self.email = email

    def introduce(self):
        print("Hi I'm ", self.name, self.id, self.email)


employee_one = Employee("emp001", "John", "john@gmail.com")
employee_one.introduce()

employee_two = Employee("emp002", "Dave")
employee_two.introduce()


class BankAccount:

    # double under, dunder functions
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

ac_one = BankAccount("AC111", "John", 1000)
ac_one.withdraw(500)
ac_one.deposit(100)

ac_two = BankAccount("AC222", "Dave", 5000)
ac_two.withdraw(500)
ac_two.deposit(100)

class Employee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def get_salary(self):
        print("Salary", self.salary)

emp = Employee("EID001", "John", 25000)
emp.get_salary()

# OOP
# Inheritance
# Abstraction
# Polymorphism
# Encapsulation