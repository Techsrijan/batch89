from tkinter import *
def Add():
    if a.get()=="" or b.get()=="":
        print("enter number")

    c=a.get()+b.get()
    res.set(c)
    print("sum=",c)

root=Tk()
root.title("Login form")
root.geometry("500x500+300+200")
root.resizable(0,0)
a=IntVar()
b=IntVar()
res=IntVar()

label=Label(root,text="ENTER First Number",fg="red",).place(x=20,y=50)
entry1=Entry(root,textvariable=a).place(x=250,y=50)
label1=Label(root,text="ENTER Second number",fg="red",).place(x=20,y=100)

entry2=Entry(root,textvariable=b).place(x=250,y=100)
btn=Button(root,text="Add",fg="white",bg="red",bd=10,font=("Times", "14", "bold italic"),command=Add).place(x=200,y=150)
lbl=Label(root,text="result",textvariable=res).place(x=200,y=300)

mainloop()
