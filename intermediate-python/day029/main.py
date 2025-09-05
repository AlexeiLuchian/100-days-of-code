from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.delete("0", END)
    pass_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    site = site_entry.get()
    mail = mail_entry.get()
    pw = pass_entry.get()

    if not site or not pw or not mail:
        messagebox.showinfo(title="Invalid Input",message="All fields must be filled.")
    else:
        yesno = messagebox.askokcancel(title=f"{site}", message=f"Are these the details you want to save?\n"
                               f"Email: {mail}\nPassword: {pw}\nClick OK to proceed.")
        if yesno:
            with open("data.txt", "a") as file:
                file.write(f"{site} | {mail} | {pw}\n")
            site_entry.delete(0, END)
            pass_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=300,height=200)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

site_label = Label(text="Website:")
site_label.grid(row=1, column=0)

mail_label = Label(text="Email/Username:")
mail_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

site_entry = Entry(width=43)
site_entry.grid(row=1, column=1, columnspan=2)
site_entry.focus()

mail_entry = Entry(width=43)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(END, "default@mail.com")

pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_pass_button = Button(text="Add", width=41, command=save_pass)
add_pass_button.grid(row=4, column=1, columnspan=2)

window.mainloop()