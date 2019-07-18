from tkinter import *
def msg():
    print("Login ho gaya")

root=Tk()
root.title("Login form")
root.geometry("500x300+300+200")
root.resizable(0,0)
frame=LabelFrame(root,text="Login Detail")
label=Label(frame,text="ENTER YOUR USER NAME",fg="red").place(x=20,y=50)
entry1=Entry(frame).place(x=250,y=50)
label1=Label(frame,text="ENTER YOUR USER PASSWORD",fg="red").place(x=20,y=100)

entry2=Entry(frame).place(x=250,y=100)
btn=Button(frame,text="Login",fg="white",bg="red",bd=10,font=("Times", "24", "bold italic"),command=msg).place(x=200,y=150)
frame.place(x=10,y=110)

mainloop()
