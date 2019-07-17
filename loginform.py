from tkinter import *
def msg():
    print("Login ho gaya")

root=Tk()
root.title("Login form")
root.geometry("500x300+300+200")
root.resizable(0,0)

label=Label(root,text="ENTER YOUR USER NAME",fg="red").place(x=20,y=50)
entry1=Entry(root).place(x=250,y=50)
label1=Label(root,text="ENTER YOUR USER PASSWORD",fg="red").place(x=20,y=100)

entry2=Entry(root).place(x=250,y=100)
btn=Button(root,text="Login",fg="white",bg="red",bd=10,font=("Times", "24", "bold italic"),command=msg).place(x=200,y=150)
mainloop()
