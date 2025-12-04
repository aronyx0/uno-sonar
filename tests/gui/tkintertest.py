import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('300x250')
root.title('Menubutton Demo')

# Menubutton variable
selected_color = tk.StringVar()

# Create the menu button
colors = ('Red', 'Green', 'Blue')

# Create the Menubutton
menu_button = ttk.Menubutton(root, text='Select a color')

# Create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=selected_color
    )


menu_button["menu"] = menu
menu_button.pack(expand=True)

def update():
    global selected_color
    label.config(text=selected_color.get())

button = ttk.Button(root, text="test", command=update)
selected_color_str = "test"
label = ttk.Label(root, text="lorem ipsum")
button.pack()
label.pack()

# Show the main window
root.mainloop()