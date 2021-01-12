import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    passwort.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website2 = website.get()
    passwort2 = passwort.get()
    email2 = email.get()
    new_data = {
        website: {
            "email": email2,
            "passwort": passwort2,
        }
    }

    if len(passwort2) == 0 or len(website2) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty!")
    else:
        try:
            with open("./data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website.delete(0, END)
            passwort.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
schloss = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=schloss)
canvas.grid(column=1, row=0)

# Entry
website = Entry(width=46)
website.grid(column=1, row=1, columnspan=2)
website.focus()

email = Entry(width=46)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, "aminkanan@hotmail.de")

passwort = Entry(width=33)
passwort.grid(column=1, row=3)

# Label
website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

email_l = Label(text="Email/Username:")
email_l.grid(column=0, row=2)

passwort_l = Label(text="Password:")
passwort_l.grid(column=0, row=3)

# Button
generate_pass = Button(text="Generate", width=10, command=generate_password)
generate_pass.grid(column=2, row=3)

add = Button(text="Add", width=39, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
