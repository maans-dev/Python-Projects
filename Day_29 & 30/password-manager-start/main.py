from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def log():
    logged_website_entry = entry_website.get()
    logged_email = entry_email.get()
    logged_ps = entry_password.get()

    is_ok = messagebox.askokcancel(title=logged_website_entry, message=f"These are the details entered: \nEmail: {email}"
                           f"\nPassword: {password} \n Is this Ok to save?")

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{logged_ps} | {logged_email} | {logged_website_entry}\n")
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="black", width=500, height=500, pady=50, padx=50)

canvas = Canvas(width=200, height=189, bg="black",  highlightthickness=0)
image_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 94.5, image=image_lock)
canvas.grid(column=1, row=0)



#Screen Layout

website = Label(text="Website:")
website.config(foreground="Red")
website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)

entry_website.focus()

email = Label(text="Email/UserName:")
email.config(bg="grey")
email.grid(column=0, row=3)

entry_email = Entry(width=35)
entry_email.grid(column=1, row=3, columnspan=2)

entry_email.insert(0, "hprademeyer123@gmail.com")

password = Label(text="Password:")
password.config(foreground="Red")
password.grid(column=0, row=4)

entry_password = Entry(width=21)

entry_password.grid(column=1, row=4, columnspan=1)

button_generated = Button(text="Generate Password")
button_generated.grid(column=3, row=4)

add_password = Button(text="Add", command=log)
add_password.grid(column=1, row=5)
add_password.config(font=("Arial", 20, "bold"))





window.mainloop()