from tkinter import *
from CONFIG import *
from tkinter import messagebox
from password_generator import generate_random_password
import pyperclip
import json


window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=PADDING_X, pady=PADDING_Y, bg=BG_COLOR)

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BG_COLOR, highlightthickness=0)
IMG_img = PhotoImage(file="logo.png")
canvas.create_image(WINDOW_HEIGHT/2, WINDOW_WIDTH/2, image=IMG_img)
canvas.grid(row=0, column=1)


def search_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website = I_website_input.get()
            try:
                email_and_password = data[website]
            except KeyError:
                messagebox.showerror(title="Error", message="There is no site under that name in your password manager")
            else:
                email = email_and_password["email"]
                password = email_and_password["password"]
                mess = f"Email: {email}\nPassword: {password}"
                messagebox.showinfo(title=website, message=mess)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There are no sites in your password manager")

def add_password():
    website = I_website_input.get()
    email = I_email_input.get()
    password = I_password_input.get()

    if website == "" or password == "" or email == "":
        messagebox.showerror(title="OOOPS", message="Don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save? ")
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                I_website_input.delete(0, END)
                I_password_input.delete(0, END)


def generate_password():
    pswrd = generate_random_password()
    I_password_input.delete(0, END)
    I_password_input.insert(0, pswrd)
    pyperclip.copy(pswrd)


L_website_label = Label(text="Website:", font=FONT, bg=BG_COLOR)
L_website_label.grid(row=1, column=0)
L_email_label = Label(text="Email/Username:", font=FONT, bg=BG_COLOR)
L_email_label.grid(row=2, column=0)
L_password_label = Label(text="Password:", font=FONT, bg=BG_COLOR)
L_password_label.grid(row=3, column=0)

I_website_input = Entry(width=50)
I_website_input.grid(row=1, column=1, columnspan=2)
I_website_input.focus()
I_email_input = Entry(width=50)
I_email_input.insert(0, "sasic.mihajlo25@gmail.com")
I_email_input.grid(row=2, column=1, columnspan=2)
I_password_input = Entry(width=31)
I_password_input.grid(row=3, column=1)

B_search = Button(text="Search", width=14, command=search_password)
B_search.grid(row=1, column=2)
B_generate_password = Button(text="Generate Password", width=14, command=generate_password)
B_generate_password.grid(row=3, column=2)
B_add = Button(text="Add", width=43, command=add_password)
B_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
