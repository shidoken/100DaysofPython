import tkinter
from tkinter import messagebox
import string
from random import choice, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(choice(characters) for x in range(randint(12, 16)))
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh No!", message="Please make sure you fill out all the fields")
    else:
        # messagebox.askokcancel(title=website, message=  f"These are the details entered: \nEmail: {email}"
        #                                                 f"\nPassword: {password} \nIs this ok to save?")
        try:
            with open("data.json", "r") as plist:
                # plist.write(f"{website}, {email}, {password}\n")
                # Reading old data
                data = json.load(plist)
        except FileNotFoundError:
            with open("data.json", "w") as plist:
                json.dump(new_data, plist, indent=4)
        # except json.JSONDecodeError:
        #     data = dict()
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as plist:
                # Saving updated data
                json.dump(data, plist, indent=4)
        finally:
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')

# ---------------------------- FIND PASSWORD --------------------------- #

def find_password():
    website = website_input.get()
    email = email_input.get()

    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Input Required", message="Please make sure you have the website and email filled out")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="No File", message="File is not created yet.")
        else:
            # new_data = data.get(website[:])
            if website in data:
                web = data[website]
                messagebox.showinfo(title="Your Saved Password", message=f"Email: {web['email']}\n Password: {web['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
            # messagebox.showinfo(title="Password Ready", message=f"Email: {newemail}\n Password: {newpassword}")
                

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# labels

website_label = tkinter.Label(text="website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="email/username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="password:")
password_label.grid(column=0, row=3)

# entries

website_input = tkinter.Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = tkinter.Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "thomasisthebest@gmail.com")
password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

# buttons

search_button = tkinter.Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
password_button = tkinter.Button(text="Generate Password", width=13, command=generate_password)
password_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
