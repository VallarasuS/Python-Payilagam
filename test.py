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

sum = add(10, 20)
print(sum)

diff = subtract(sum, 1)
print(diff)

exp = mul(sum, 3)
print(exp)

greet()