from tkinter import *

window = Tk()
window.title("Hello World")
window.geometry("800x600")

button = Button(window)
button.configure(text="Click Me")
button.pack()

window.mainloop()
