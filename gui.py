# Program starts by incorportaing Tk
from tkinter import *
from tkinter import ttk

# ttk is a submodule of tkinter. It implements Python's binding
# to the newer "themed widgets" that were added to Tk in 8.5


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = Tk()  # Sets up the main application window
root.title("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")  # Window title

# Here we are defining our frame widget, for the contents of our user interface
mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(
    column=0, row=0, sticky=(N, W, E, S)
)  # grid places it directly inside our main application window

# Two lines below should expand to fill any extra space if the window is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  # Entry will be a textbox
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W
)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
