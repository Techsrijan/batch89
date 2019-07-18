from tkinter import *
from tkinter import ttk
'''def get():
    print(sp.get())'''

def getradio():
    print(i.get())
    print(j.get())
    print(k.get())
    print(l.get())
    print(m.get())
root=Tk()

#sp=Spinbox(root, from_=1 ,to=4,).pack()
#height=no of character
txt=Text(root,height=2,width=3).pack()
f=Frame(root)
i=IntVar()
r=Radiobutton(f,text="male",value=1,variable=i)
r1=Radiobutton(f,text="female",value=2,variable=i)
r.pack()
r1.pack()
f.pack()

w = Scale(root, from_=0, to=42)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()


j=IntVar()
f1=Frame(root)
r2=Radiobutton(f1,text="DayScholor",value=1,variable=j)
r3=Radiobutton(f1,text="Hostler",value=2,variable=j)
r2.pack()
r3.pack()
f1.pack()

k=IntVar()
c=Checkbutton(root,text="hindi",variable=k)
l=IntVar()
c1=Checkbutton(root,text="english",variable=l)
m=IntVar()
c2=Checkbutton(root,text="Urdu",variable=m)
c.pack()
c1.pack()
c2.pack()

l=Listbox(root,width=50)
l.insert(3,"JAVAsahdsahdkashdkashdkadhkadhakdhkadhaks")
l.insert(2,"PHP")
l.insert(1,"PYTHON")
l.pack()



labelTop = Label(root,text = "Choose your favourite month")
labelTop.pack()

comboExample =ttk.Combobox(root,values=[
                                    "January",
                                    "February",
                                    "March",
                                    "April"])
print(dict(comboExample))
comboExample.pack()
comboExample.current(1)

print(comboExample.current(), comboExample.get())






btn=Button(root,text="Login",fg="white",bg="red",bd=10,font=("Times", "24", "bold"),command=getradio).pack()


mainloop()