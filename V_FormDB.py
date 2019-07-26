from tkinter import *

root = Tk()
root.geometry("350x400+500+150")
root.title("MyDBform")
root.resizable(0,0)

def submit():

    top = Toplevel()
    top.resizable(0,0)
    top.geometry("350x400+500+150")
    label= Label(top,text="Your Account Details",fg="green", bd=5, bg="black",width=30,height=2, font=("Ariel",12,"bold")).place(x=20,y=0)

    btn_logout= Button(top,text="LogOuT",width=28,bd=5, relief=GROOVE,command=login).place(x=65, y=100)

    mainloop()


def login():
    label= Label(root,text="Account Information",fg="green", bd=5, bg="black",width=30,height=2, font=("Ariel",12,"bold")).place(x=20,y=0)
    label = Label(root,text="User Name").place(x=65,y=55)
    entry1=Entry(root).place(x=145,y=55)

    label = Label(root, text="Password").place(x=65, y=80)
    entry2 = Entry(root,show="*").place(x=145,y=80)

    btn= Button(root,text="Login",width=28,bd=5, relief=GROOVE,command=submit).place(x=65, y=120)

login()





mainloop()