from tkinter import *
def msg():
    s1=s.get()
    print(s1)

root=Tk()
root.title("Login form")
root.geometry("500x300+300+200")
root.resizable(0,0)
s=StringVar()
label=Label(root,text="ENTER YOUR USER NAME",fg="red").place(x=20,y=50)
entry1=Entry(root,textvariable=s).place(x=250,y=50)

btn=Button(root,text="Get User Name",fg="white",bg="red",bd=10,font=("Times", "16", "bold italic"),command=msg).place(x=200,y=150)

mainloop()
