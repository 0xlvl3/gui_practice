import customtkinter

customtkinter.set_appearance_mode("dark")  # System theme for our application
customtkinter.set_default_color_theme("dark-blue")  # Color theme for our application

root = customtkinter.CTk()
root.geometry("750x530")
root.title("Flashcards")


def login():
    print("test")


# login menu
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# after login
frame2 = customtkinter.CTkFrame(master=root)
frame.pack()

label = customtkinter.CTkLabel(
    master=frame,
    text="Login System",
)
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)


entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="$")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

dropdown = customtkinter.CTkComboBox(
    master=frame, values=["options1", "options2", "options3"]
)
dropdown.pack(padx=20, pady=10)
dropdown.set("options1")


root.mainloop()
