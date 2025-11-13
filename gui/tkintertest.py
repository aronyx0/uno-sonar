from tkinter import *
import tkinter
from tkinter.ttk import Menubutton
 
def f():
  var.set("Food")
 
root = Tk()
 
var = StringVar()
 
mb = Menubutton (root, textvariable = var)
mb.pack()
menu =  Menu ( mb, tearoff = 0 )
mb["menu"] = menu
 
b = Button(root, text = "Click", command = f)
b.pack()
 
mayoVar = IntVar()
ketchVar = IntVar()
 
menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )
 
mb.pack()
root.mainloop()