import tkinter as tk


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root 

def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text="Sem conta ainda",
        anchor='e', justify='right', background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5, sitcky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=0, column=0, columnspan=5, sitcky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        hightlighttthickness=1, hightlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display 

def display_control_a(event):
    event.widget.select_range(0,'end')
    event.widget.icursor('end')
    return 'break'