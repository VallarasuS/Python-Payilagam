# from tkinter import *

# window = Tk()
# window.title("Hello World")
# window.geometry("800x600")

# button = Button(window)
# button.configure(text="Click Me")
# button.pack()

# window.mainloop()

from maths import add, power
from hello import greet, subtract
from OOP.bank_account import BankAccount

sum = add(10, 20)
print(sum)

diff = subtract(sum, 1)
print(diff)

exp = mul(sum, 3)
print(exp)

greet()

account = BankAccount("Rob", "ACB3322", 5000)
account.deposit(100)