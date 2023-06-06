# A GUI program to generate random password based on user inputted password length

import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    length = int(length_entry.get())
    if length < 6:
        messagebox.showerror("Length Error", "Length of Password should be greater than 6")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)


window = tk.Tk()
window.title("Random Password Generator")

length_label = tk.Label(window, text="Enter Password Length")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="GENERATE PASSWORD", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="Generated Password")
password_label.pack()

password_entry = tk.Entry(window)
password_entry.pack()

window.mainloop()
