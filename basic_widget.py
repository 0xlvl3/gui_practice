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
# Our action will come from a callback command.
def print_hello():
    print("hello")


# In our button_hello we place our callback function print_hello as our command
button_hello = ttk.Button(root, text="say hello", command=print_hello).grid(
    column=0, row=0
)
button_exit = ttk.Button(root, text="don't click me : )", command=exit)
button_exit.grid(column=1, row=1)
button_exit.state(["disabled"])


def test():
    print(random_var)


random_var = StringVar()
check = ttk.Checkbutton(
    root,
    text="Check this",
    command=test,
    variable=random_var,
    onvalue="on",
    offvalue="off",
)
check.grid(column=4, row=1)


# Linked by the phone variable clicking one Radiobutton the others will check
phone = StringVar()
home = ttk.Radiobutton(root, text="Home", variable=phone, value="home")
yellow = ttk.Radiobutton(root, text="yellow", variable=phone, value="yellow")
tt = ttk.Radiobutton(root, text="test", variable=phone, value="test")
home.grid(column=5, row=5)
yellow.grid(column=6, row=5)
tt.grid(column=7, row=5)


# Text field testing.

username = StringVar()
name = ttk.Entry(root, textvariable=username)
name.grid(column=10, row=10)
name_label = Label(root)


def show_text():
    text = name.get()
    name_label = print(text)


text_button = Button(root, text="show text", command=show_text)

text_button.grid(column=11, row=10)
name_label.grid(column=12, row=10)

name.insert(0, "Your name")  # In text field


string_var = StringVar()
text_entry = Entry(root, textvariable=string_var)
show_label = Label(root, textvariable=string_var)

text_entry.grid(column=10, row=0)
show_label.grid(column=11, row=0)

# Password Entry.

password = StringVar()
passwd = ttk.Entry(root, textvariable=password, show="#")
passwd.grid(column=9, row=0)


root.mainloop()
