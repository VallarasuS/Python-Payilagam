from tkinter import *
from tkinter import ttk

# Root / Shell / Window
root = Tk()
root.title("Hello")
root.geometry("800x500")

# x = 10  # INT
stringVariable = StringVar()


def OnButtonClicked():
    # print("Button was clicked")
    # text = entry.get()
    text = stringVariable.get()
    # print(text)
    # stringVariable.set("Cleared")

    contact = ttk.Label(root, text=text)
    contact.pack()


# widgets, control, elements, components
label = ttk.Label(root, text="Hello World")
label.pack()

# value bound to string variable
entry = ttk.Entry(root, textvariable=stringVariable)
entry.pack()

# event handling
# event wiring
# event binding
button = ttk.Button(root, text="Add", command=OnButtonClicked)
button.pack()

root.mainloop()


# def add (x, y):
#     return x + y


# add(10, 20)
# add(x= 10, y=20)
