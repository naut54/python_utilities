import tkinter as tk
import pyperclip
from tkinter import messagebox
import html_generator, password_generator

b_c = "black"
f_c_1 = "white"
f_c_2 = "green"
f_c_3 = "white"

class app_1:
    def __init__(self, root):
        self.root = root
        self.root.title("Utilities Suite")
        self.root.geometry("300x100")
        self.root.configure(bg = b_c)
        
        self.button1 = tk.Button(root, text="Generate WEB Structure", command = self.web_e)
        self.button1.pack(pady=10)
        self.button1.configure(fg = f_c_3, bg = b_c)
        
        self.button1 = tk.Button(root, text="Password generator", command = self.pas)
        self.button1.pack(pady=10)
        self.button1.configure(fg = f_c_3, bg = b_c)
        
        self.v = tk.Label(root, text = "Versión 1.0.3")
        self.v.pack(side="bottom", anchor="sw")
        self.v.configure(fg = f_c_2, bg = b_c)
    def web_e(self):
        html_generator.create_complex_folder_structure()
    
    def pas(self):
        password_generator.ac()

if __name__ == "__main__":
    root = tk.Tk()
    app = app_1(root)
    root.mainloop()