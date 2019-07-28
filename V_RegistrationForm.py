from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def alertmsg():
    confirm=messagebox.askyesnocancel("Save File",'Do you want to save file. Press "OK"')
    #confirm =messagebox.showwarning("Save File",'Do you want to save file. Press "OK"')
    if confirm==True:
        get_data()
        quit()
    elif confirm==False:
        pass
    else:
        quit()



def get_data():
    """print(fn.get())
    print(ln.get())
    print(d.get())
    print(em.get())
    print(mo.get())
    print(i.get())
   # print(ad.get())
    print(ct.get())
    print(pc.get())
    print(st.get())
    6-+print(cn.get())"""

    print("First Name :",fn.get())
    print("Last Name :",ln.get())
    print("Date of Birth :",d.get())
    print("E-mail :",em.get())
    print("Mobile :",mo.get())
    #print("Gender :",g.get())
    if g.get()==1:
        print("Gender : Male")
    else:
        print("Gender : Female")

    print("Address :",ad.get())
    print("City :",ct.get())
    print("PinCode :",pc.get())
    print("State :",st.get())
    print("Country :",cn.get())







root = Tk()
root.geometry("300x400+500+150")
root.title("My form")
root.resizable(0,0)

#frame = LabelFrame(root, text="Registration Form")

fname =Label(root, text="First Name").place(x=10,y=10)
fn=StringVar()
entry1 = Entry(root,textvariable=fn).place(x=150,y=10)


lname =Label(root, text="Last Name").place(x=10,y=35)
ln = StringVar()
entry2 = Entry(root,textvariable=ln).place(x=150,y=35)


dob =Label(root, text="Date of Birth").place(x=10,y=60)
d=IntVar()
entry3 = Entry(root,textvariable=d).place(x=150,y=60)


email =Label(root, text="E-mail").place(x=10,y=85)
em = StringVar()
entry3 = Entry(root,textvariable=em,bd=1).place(x=150,y=85)


mob =Label(root, text="Mobile No.").place(x=10,y=110)
mo = IntVar()
entry4 = Entry(root,textvariable=mo).place(x=150,y=110)


gender = Label(root, text="Gender").place(x=10,y=135)
g = IntVar()
m=Radiobutton(root,text="Male",value=1,variable=g).place(x=150,y=135)
f=Radiobutton(root,text="Female",value=2,variable=g).place(x=210,y=135)


address =Label(root, text="Address").place(x=10,y=160)
ad = StringVar()
entry5 = Text(root,height=3,width=15).place(x=150,y=160)


city = Label(root, text="City").place(x=10,y=220)
ct = StringVar()
menu = ttk.Combobox(root,value=["Gorakhpur","Kushinagar","MaharajGanj","Khalilabaad","Basti"],width=17,textvariable=ct).place(x=150,y=220)
#menu.current(0)


pn=Label(root,text="PinCode").place(x=10,y=245)
pc= IntVar()
entry7=Entry(root,textvariable=pc).place(x=150,y=245)


state = Label(root,text="State").place(x=10,y=270)
st = StringVar()
entry8 = ttk.Combobox(root, value=["Uttar Pradesh","Madhya Pradesh","Gujarat","Uttrakhand","Rajasthan"],width=17,textvariable=st).place(x=150,y=270)


country= Label(root,text="Country").place(x=10,y=295)
cn= StringVar()
entry9 = ttk.Combobox(root,value=["India","Afganistaan","USA","UK","Izrail"],textvariable=cn,width=17).place(x=150,y=295)

btn =Button(root,activebackground="red",state=ACTIVE, activeforeground="orange",highlightcolor="blue",text="SUBMIT",bd=4,justify=CENTER,command=alertmsg).place(x=125,y=345)
#frame.place(x=0,y=100)
mainloop()