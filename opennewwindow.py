from tkinter import *

def open_window():
    top=Toplevel(root)
    top.title("top window")
    btn1 = Button(top, text="close", command=top.destroy).pack()
    top.geometry("400x400+400+200")


root=Tk()
root.title("Main window")
btn=Button(root,text="open new window",command=open_window)
btn.pack()
root.geometry("400x400+400+200")
mainloop()