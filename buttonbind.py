from tkinter import *

'''def msg():
    print("Good morning")'''


def leftclik(event):
    print("Good morning")

def middleclik(event):
    print("Good afternoon")

def rightclik(event):
    print("Good night")
root =Tk()
#button=Button(root,text="click me",command=msg)


button=Button(root,text="click me")
button.bind("<Button-1>",leftclik)
button.pack()

button1=Button(root,text="click me1")
button1.bind("<Button-2>",middleclik)
button1.pack()

button2=Button(root,text="click me2")
button2.bind("<Button-3>",rightclik)
button2.pack()
mainloop()