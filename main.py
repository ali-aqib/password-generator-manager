from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_file():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please dont leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword: {password} \n Is it OK to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)
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

add_button = Button(text="Add", width=44, relief="groove", command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "dummy@xyz.com" )

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

window.mainloop()