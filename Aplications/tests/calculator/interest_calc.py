import tkinter as tk
from tkinter import messagebox

class int_calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de interés")
        self.root.geometry("300x400")
        self.root.iconbitmap("C:/Users/admin/Documents/GitHub/python_utilities/Aplications/tests/calculator/calculator.ico")

if __name__ == "__main__":
    root = tk.Tk()
    app = int_calc(root)
    root.mainloop()