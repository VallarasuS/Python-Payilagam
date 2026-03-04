from tkinter import *
from tkinter import Tk, ttk


# Pack
# Grid
# Place

# root window / shell
root = Tk()
root.title("Hello Grid")
root.geometry("800x500")

# expand, fill, fit available space
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# layout container - panel, canvas, shell
frame = ttk.Frame(root)
frame.grid()

# Grid Layout 3x2
# -----------------
#    0,0   |   0,1
# -----------------
#    1,0   |  1,1
# -----------------
#    2,0   |  2,1
# -----------------


def on_add_clicked():
    print(name_entry.get())
    print(phone_entry.get())


# Name - Row 0

name = ttk.Label(frame, text="Name")
name.grid(row=0, column=0, padx=10, pady=10)

name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Phone - Row 1

phone = ttk.Label(frame, text="Phone")
phone.grid(row=1, column=0, padx=10, pady=10)

phone_entry = ttk.Entry(frame)
phone_entry.grid(row=1, column=1, padx=10, pady=10)

# Add Button - Row 2

add_button = ttk.Button(frame, text="Add", command=on_add_clicked)
add_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

root.mainloop()
