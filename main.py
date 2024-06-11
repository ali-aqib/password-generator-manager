from tkinter import *
def close_window():
    window.destroy()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=50)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Buttons
gen_pass_button = Button(text="Generate Password", relief="groove")
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, relief="groove")
add_button.grid(row=4, column=1, columnspan=2, pady=5)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "jacksonsam786@gmail.com" )

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

window.after(10000, close_window)

window.mainloop()