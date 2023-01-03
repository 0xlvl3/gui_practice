from tkinter import ttk
from tkinter import *

# https://tkdocs.com/tutorial/widgets.html

# Frames are created using Frame class
# frame = ttk.Frame(parent) = parent here is == root

root = Tk()
s = ttk.Style()  # store Style class in s
s.configure(
    "Danger.TFrame", background="red", borderwidth=5, relief="raised"
)  # Configure style class here

frame = ttk.Frame(
    root, width=200, height=200, style="Danger.TFrame"
).grid()  # Giving our Frame class configuration

# Label is a widget that displays test or images.

label = ttk.Label(root, text="test test test")
label.grid(column=0, row=0)
label2 = ttk.Label(root, text="this is another label")
label2.grid(column=1, row=0)
label3 = ttk.Label(root, text="another one")
label3.grid(column=2, row=2)
label4 = ttk.Label(root, text="Just another test").grid(column=3, row=0)

# Multi-line labels can be displayed as well. with \n

# Button
# Buttons are meant to be interacted with. Pressing a button should perform some action.

button = ttk.Button(root, text="press me", command=exit)
button.grid(column=0, row=0)

root.mainloop()
