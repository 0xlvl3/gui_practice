import tkinter as tk

bg_color = "#3d6466"

# Initiallize app.
root = tk.Tk()
root.title("Test")


# def clear_widgets(frame):
#    for widget in frame.winfo_children():
#        widget.destory()


def login_frame():
    #    clear_widgets(home)
    login.tkraise()
    login.pack_propagate(False)  # Prevent child from modifying parent

    question = tk.Label(login, text="test test test").pack()

    button = tk.Button(
        login,
        text="Click me",
        font=("TkHeadingFont", 20),
        fg="white",
        cursor="hand2",
        command=lambda: home_page(),
    ).pack()


def home_page():
    # clear_widgets(login)
    home.tkraise()
    home.pack_propagate(False)

    question = tk.Label(home, text="You did it").pack()
    button = tk.Button(
        home, text="click this to go back to menu", command=lambda: login_frame()
    ).pack()


login = tk.Frame(root, width=500, height=600, bg=bg_color)
home = tk.Frame(root, bg=bg_color)

for frame in (login, home):
    frame.grid(row=0, column=0)

login_frame()

# Mainloop.
root.mainloop()
