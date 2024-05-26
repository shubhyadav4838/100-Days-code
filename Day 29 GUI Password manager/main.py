from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not web or not password:
        messagebox.showinfo(title="OOPS", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            file = "100 Days code/Day 29 GUI Password manager/data.txt"
            with open(file,"a") as data:
                data.write(f"{web} | {email} | {password}\n")
            website_entry.delete(0,END)  
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager!")
window.config(padx=50, pady=50)

canvas = Canvas(width = 200, height = 200,highlightthickness=0 )
lock_img = PhotoImage(file = "100 Days code/Day 29 GUI Password manager/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Inputs
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1,columnspan=2)
website_entry.focus() # Focus on the entry field

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0,"shubhyadav@gmail.com")

password_entry = Entry(width=33, show='*')
password_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=44, command= save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
