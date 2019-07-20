from tkinter import*
def btnClick(number):
    global val
    val=val + str(number)
    data.set(val)
def btnClear():
    global val
    val=""
    data.set("")
def btnEquals():
    global val
    sum=str(eval(val))
    data.set(sum)

root=Tk()
root.geometry("300x400+150+200")
root.resizable(0,0)
root.title("calculator")
val=""
data=StringVar()
label=Label(root,text="Label",anchor=SE,font=("verdana",20),textvariable=data,background="#ffffff",fg="#000000")
label.pack(expand=True,fill="both")


btnrow1=Frame(root,bg="#000000")
btnrow1.pack(fill="both",expand=True)



btnrow2=Frame(root)
btnrow2.pack(fill="both",expand=True)

btnrow3=Frame(root)
btnrow3.pack(fill="both",expand=True)

btnrow4=Frame(root)
btnrow4.pack(fill="both",expand=True)

button7=Button(btnrow1,text="7",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(7))
button7.pack(side=LEFT,fill="both",expand=True)

button8=Button(btnrow1,text="8",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(8))
button8.pack(side=LEFT,fill="both",expand=True)

button9=Button(btnrow1,text="9",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(9))
button9.pack(side=LEFT,fill="both",expand=True)

button=Button(btnrow1,text="+",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick("+"))
button.pack(side=LEFT,fill="both",expand=True)









button2=Button(btnrow2,text="4",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(4))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow2,text="5",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(5))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow2,text="6",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(6))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow2,text="-",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick("-"))
button2.pack(side=LEFT,fill="both",expand=True)






button2=Button(btnrow3,text="1",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(1))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow3,text="2",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(2))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow3,text="3",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick(3))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow3,text="*",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick("*"))
button2.pack(side=LEFT,fill="both",expand=True)


button2=Button(btnrow4,text="c",font=("verdana",22),relief=GROOVE,border=0,command=btnClear)
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow4,text="0",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick("0"))
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow4,text="=",font=("verdana",22),relief=GROOVE,border=0,command= btnEquals)
button2.pack(side=LEFT,fill="both",expand=True)

button2=Button(btnrow4,text="/",font=("verdana",22),relief=GROOVE,border=0,command=lambda:btnClick("/"))
button2.pack(side=LEFT,fill="both",expand=True)




root.mainloop()
