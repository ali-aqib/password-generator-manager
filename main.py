from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = ([choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))]
                     + [choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_to_file():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="Oops", message="Please dont leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \n Is it OK to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                username_entry.delete(0, END)

# --------------------------FIND PASSWORD------------------------------ #


def find_password():
    website = website_entry.get().title()
    if website == "":
        messagebox.showwarning(title="Oops", message="Please type a website to search.")
    else:
        try:
            with open("data.json") as file:
                data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(title="OPPS", message="You have not saved any passwords yet")
        except KeyError:
            messagebox.showinfo(title="OOPS", message="Credentials Not Found")
        else:
            messagebox.showinfo(title=f"Details Found for {website}", message=f"Email: {email}\n Password: {password}\n"
                                                                              f"Password copied to clipboard.")
            pyperclip.copy(password)

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
gen_pass_button = Button(text="Generate Password", relief="groove", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, relief="groove", command=write_to_file)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

search_button = Button(text="Search", relief="groove", width=14, command=find_password)
search_button.grid(row=1, column=2)

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
# If write an email in the username entry, uncomment the below line and insert your email at the place of dummy@xyz.com
# username_entry.insert(0, "dummy@xyz.com" )

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

window.mainloop()
