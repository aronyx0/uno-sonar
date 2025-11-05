import tkinter as tk
from tkinter import ttk

def fn():
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lorem Ipsum")
    root.geometry("600x600")
    root.resizable(False, False)
    contents = []

    contents.append(ttk.Button(root, text="quit", command=lambda: root.quit()))
    contents.append(ttk.Label(root, text="hell yeah"))
    for item in contents:
        item.pack()

    root.mainloop()