from tkinter import *
def msg():
    print("hi")
root=Tk()
main_menu=Menu(root)
root.config(menu=main_menu)
filemenu=Menu(main_menu)
main_menu.add_cascade(label="FILE",menu=filemenu)
filemenu.add_command(label="New Project",command=msg)
filemenu.add_command(label="OPEN Project",command=msg)
filemenu.add_separator()
filemenu.add_command(label="Save Project",command=msg)
filemenu.add_command(label="Save as Project",command=msg)
filemenu.add_command(label="exit",command=quit)
editmenu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=editmenu)
t=Text(root)
t.pack(fill=BOTH,expand=1)
mainloop()