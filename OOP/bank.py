p1_balance = 1000
p2_balance = 2000

def deposit(balance, amount):
    balance = balance + amount

def withdraw(balance, amount):
    balance = balance - amount


deposit(p1_balance, 100) # 1100
withdraw(p1_balance, 200) # 900

deposit(p2_balance, 100)
withdraw(p2_balance, 100)