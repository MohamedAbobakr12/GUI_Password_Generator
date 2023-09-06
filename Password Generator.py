import customtkinter as ctk
import string
import random

app = ctk.CTk()
app.geometry("640x480")
app.iconbitmap("Password.ico")
app.title("Password Generator")
Label1 = ctk.CTkLabel(app, text='Password Generator', font=('Arial', 30), text_color='#7AE582')
Label1.pack()

letter_store = ctk.StringVar(value="")

length = ctk.IntVar()
x = ctk.IntVar()
y = ctk.IntVar()
z = ctk.IntVar()
str = ctk.StringVar()


def letters():
    all_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_characters = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    all_digits = '01234567890123456789012345678901234567890123456789'
    if (x.get() == 1 and z.get() == 1 and y.get() == 0):
        all = all_letters + special_characters
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (x.get() == 1 and y.get() == 1 and z.get() == 0):
        all = special_characters + all_digits
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (z.get() == 1 and y.get() == 1 and x.get() == 0):
        all = all_letters + all_digits
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (x.get() == 1 and y.get() == 1 and z.get() == 1):
        all = all_letters + all_digits + special_characters
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (x.get() == 0 and y.get() == 0 and z.get() == 1):
        all = all_letters
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (x.get() == 0 and y.get() == 1 and z.get() == 0):
        all = all_digits
        password = "".join(random.sample(all, length.get()))
        str.set(password)
    elif (x.get() == 1 and y.get() == 0 and z.get() == 0):
        all = special_characters
        password = "".join(random.sample(all, length.get()))
        str.set(password)


Entry1 = ctk.CTkEntry(app, width=300, height=30, state='readonly', textvariable=str, text_color='#7AE582')
Entry1.place(x=167, y=45)

Checkbox1 = ctk.CTkCheckBox(app, width=100, text='Letters', variable=z, onvalue=1, offvalue=0)
Checkbox1.place(x=45, y=250)

Checkbox2 = ctk.CTkCheckBox(app, width=100, text=' Special Characters', variable=x, onvalue=1, offvalue=0)
Checkbox2.place(x=45, y=290)

Checkbox3 = ctk.CTkCheckBox(app, width=100, text='Numbers', variable=y, onvalue=1, offvalue=0)
Checkbox3.place(x=45, y=330)

Label2 = ctk.CTkLabel(app, text="Length", font=('Arial', 20), text_color='#7AE582')
Label2.place(x=395, y=240)

Entry2 = ctk.CTkEntry(app, width=150, height=15, textvariable=length)
Entry2.place(x=395, y=270)

Button1 = ctk.CTkButton(app, text='Generate', font=('Arial', 25), text_color='#0E103D', fg_color='#7AE582',
                        command=lambda: print(letters()))
Button1.place(x=250, y=380)

app.mainloop()
