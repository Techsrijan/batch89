from tkinter import *
def getvalue():
    s=txt.get(1.0,END)
    print(s)

def getselect():
    s=txt.selection_get()
    print(s)

def clear():
    txt.delete(1.0,END)

def getSelectPosition():
    s = txt.selection_get()
    pos=txt.search(s,1.0,stopindex=END)
    print(pos)

root=Tk()
txt=Text(root,height=5,width=30,wrap=WORD,padx=10,pady=10,bd=5,selectbackground="red")
txt.insert(INSERT,"Welcome you all")
txt.pack()
btn=Button(root,text="Print ALL",fg="white",bg="red",bd=10,font=("Times", "12", "bold"),command=getvalue).pack()

btn1=Button(root,text="Selected Print",fg="white",bg="red",bd=10,command=getselect).pack()

btn_clear=Button(root,text="Delete",fg="white",bg="red",bd=10,command=clear).pack()

btn_Select_Pos=Button(root,text="Selected Element Psition",fg="white",bg="red",bd=10,command=getSelectPosition).pack()
mainloop()