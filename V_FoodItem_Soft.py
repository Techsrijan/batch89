from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("350x400+500+150")
root.title("Billing System")
root.resizable(0,0)


def bill():
    no_of_items=n.get()
    total_price=no_of_items * rs_price.get()
    tax=total_price*5/100
    total=total_price + tax
    print(total)

    res.set(total)



label = Label(root, text="****Food Restaurant****",justify="center", fg="green", bd=5, bg="yellow", width=25, height=2,font=("Ariel", 15, "bold")).place(x=20, y=5)

food_item=Label(root,text="Food Item",font=("Ariel", 12, "bold")).place(x=65,y=95)
#entry1 = Entry(root).place(x=145, y=55)
items=ttk.Combobox(root, value=["Veg Biryani","Roti","Green Salad","Paneer Tikka","Paneer DoPyaza","Chicken Tanduri","Half Fry","Mutton"]).place(x=155,y=95)

quantity=Label(root,text="Quantity",font=("Ariel", 12, "bold")).place(x=65,y=130)
n=IntVar()
num=ttk.Combobox(root,value=list(range(1,10)), textvariable=n).place(x=155,y=130)

price=Label(root,text="Price",font=("Ariel", 12, "bold")).place(x=65,y=165)
rs_price=IntVar()
rs=Entry(root,width=23,bd=2,textvariable=rs_price).place(x=155,y=165)


btn= Button(root,text="Big total with 5% GST",bg="pink",justify="center",bd=2,font=("Ariel", 12, "bold"),command=bill).place(x=85,y=220)

total_bill=Label(root,text="Total Amount",font=("Ariel", 12, "bold")).place(x=45,y=290)

res=IntVar()
txt=Entry(root,textvariable=res).place(x=175,y=290)

mainloop()