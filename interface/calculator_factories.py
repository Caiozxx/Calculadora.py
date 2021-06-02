import tkinter as tk

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root