from tkinter import *

def msg(event=""):
    print("hi")


def getlistdata():
    selecteditem=l.curselection()
    print(selecteditem)
    for item in selecteditem:
        print(l.get(item))

def deletedata():
    selecteditem = l.curselection()
    for item in selecteditem:
        print(l.delete(item))

root=Tk()
root.bind('<Control-r>',msg)
l=Listbox(root,width=50,selectmode=MULTIPLE)
l.insert(3,"JAVAsahdsahdkashdkashdkadhkadhakdhkadhaks")
l.insert(2,"PHP")
l.insert(1,"PYTHON")
l.pack()
btn=Button(root,text="getdata",fg="white",bg="red",bd=10,font=("Times", "12", "bold"),command=getlistdata)

btndelete=Button(root,text="deleteitem",fg="white",bg="red",bd=10,font=("Times", "12", "bold"),command=deletedata)
btn.pack()
btndelete.pack()
btnmsg=Button(root,text="msg",command=msg).pack()
mainloop()
