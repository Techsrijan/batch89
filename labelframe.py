from tkinter import *
def msg():
    print("Login ho gaya")

root=Tk()
root.title("Login form")
root.geometry("500x300+300+200")
root.resizable(0,0)
frame=LabelFrame(root,text="Login Detail")
label=Label(frame,text="ENTER YOUR USER NAME",fg="red").pack()
entry1=Entry(frame).pack()
label1=Label(frame,text="ENTER YOUR USER PASSWORD",fg="red").pack()

entry2=Entry(frame).pack()
btn=Button(frame,text="Login",fg="white",bg="red",bd=10,font=("Times", "24", "bold italic"),command=msg).pack()
frame.pack()

mainloop()