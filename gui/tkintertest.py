import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lorem Ipsum")
    root.geometry("600x600")
    root.resizable(False, False)
    ttk.Combobox(root).pack()
    root.mainloop()