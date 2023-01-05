import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")  # System theme for our application
customtkinter.set_default_color_theme("dark-blue")  # Color theme for our application

root = customtkinter.CTk()
root.title("Flashcards")


# Login screen
def login_screen():
    login.tkraise()
    # login menu
    login.pack_propagate(False)

    label = customtkinter.CTkLabel(
        master=login,
        text="Login System",
    )
    label.pack()

    entry1 = customtkinter.CTkEntry(master=login, placeholder_text="Username")
    entry1.pack()

    entry2 = customtkinter.CTkEntry(master=login, placeholder_text="Password", show="$")
    entry2.pack()

    button = customtkinter.CTkButton(
        master=login, text="Login", command=lambda: homepage_screen()
    )
    button.pack()

    checkbox = customtkinter.CTkCheckBox(master=login, text="Remember me")
    checkbox.pack()


def homepage_screen():
    homepage.tkraise()
    homepage.pack_propagate(False)

    homepage.pack()

    test = customtkinter.CTkLabel(master=homepage, text="You made it")
    test.pack()


login = customtkinter.CTkFrame(master=root, width=500, height=600)
homepage = customtkinter.CTkFrame(master=root)

for frame in (login, homepage):
    frame.pack()

login_screen()
root.mainloop()
