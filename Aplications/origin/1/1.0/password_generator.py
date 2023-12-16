import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox

b_c = "black"
f_c_1 = "white"
f_c_2 = "green"
f_c_3 = "white"

class p_g:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x100")
        self.root.configure(bg=b_c)

        self.button1 = tk.Button(root, text="Generate a password", command=self.generate_and_print_password)
        self.button1.pack(pady=30)
        self.button1.configure(fg=f_c_3, bg=b_c)

    def generate_random_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_and_print_password(self):
        length = self.ask_for_number("Desired length:")
        if length is not None:
            password = self.generate_random_password(length)
            messagebox.showinfo("Your password", password)

    def ask_for_number(self, prompt):
        try:
            result = simpledialog.askinteger(" ", prompt)
            return result
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese un número válido.")
            return None


def ac():
    root = tk.Tk()
    app = p_g(root)
    root.mainloop()

ac()
