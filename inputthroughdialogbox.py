from tkinter import *
from tkinter import simpledialog
def get_value():
    s= simpledialog.askstring("Input Value","Input Your Name")
    print(s)


root = Tk()
btn= Button(root,text="click to popup", command=get_value).pack()

mainloop()