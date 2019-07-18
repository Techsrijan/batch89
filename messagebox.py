from tkinter import *
from tkinter import messagebox
def msg():
    s=messagebox.askyesnocancel("Save File","do u want to save file")
    #t=messagebox.showwarning("age overflow","Age can not be less than zero")
    #u=messagebox.showerror("age overflow","Age can not be less than zero")
    print(s)
    if s==True:
        print("save file")
    else:
        quit()

root= Tk()

button=Button(root,text="click me",command=msg)
button.pack()

mainloop()