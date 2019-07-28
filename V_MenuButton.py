from tkinter import *

top = Tk()

top.geometry("200x250")

menubutton = Menubutton(top, text="Language", relief=FLAT)

menubutton.grid()

menubutton.menu = Menu(menubutton)

menubutton["menu"] = menubutton.menu
menubutton.menu.add_separator()
menubutton.menu.add_checkbutton(label="Hindi", variable=IntVar())

menubutton.menu.add_checkbutton(label="English", variable=IntVar())

menubutton.pack()

top.mainloop()