from tkinter import *
import pymysql
from tkinter import messagebox,ttk

# from  V_FoodItem_Soft import billz
bill = Tk()
bill.title("Food Billing")
bill.geometry("805x665+280+10")
bill.resizable(0,0)

########################## create treeview###############################################################
displayDB=ttk.Treeview(height=15, columns=('Rate', 'Quantity', 'Cost'))

####################################### Database connectivity###################################################################################
def dbconfig():
    global conn,mycursor
    conn = pymysql.connect(host="localhost",user="root",db="restaurant")
    mycursor=conn.cursor()


####################################### main heading###################################################################################
def main_heading():
    label=Label(bill,text="Food Management System",fg="green", bd=5, bg="yellow", width=59, height=2,font=("Algerian", 15, "bold")).grid(row=0, column=0, columnspan=4, padx=(10, 0), pady=(10, 0))

######################################### First Window###################################################################################
def firstwindow():
    remove_all_widgets()
    main_heading()

    admin_btn = Button(bill, text="Admin Login", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=loginwindow).grid(row=1, column=0, columnspan=1)
    label=Label(text="").grid(row=5,column=4)
    guest_btn = Button(bill, text="Guest Login", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=Guest).grid(row=1, column=3, columnspan=1)



####################################### Login Window ###################################################################################
def loginwindow():
    """username = Label(bill, text="User", font=("Ariel", 12, "bold")).place(x=65, y=95)
    enrty1=Entry(bill,textvariable=user).place(x=155,y=95)

    password = Label(bill, text="Password", font=("Ariel", 12, "bold")).place(x=65, y=130)
    enrty2 = Entry(bill,textvariable=passs).place(x=155, y=130)

    btn = Button(bill, text="Login", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=adminlogin).place(x=105, y=220)"""

    remove_all_widgets()
    main_heading()
    back_4_first_window()
    label = Label(text="Admin Login",fg="blue", bd=5, bg="sky blue", width=25, height=2,font=("Times New Roman", 12, "bold")).grid(row=1, column=1, columnspan=2)

    username = Label(bill, text="User", font=("Ariel", 12, "bold"))
    username.grid(row=2, column=1, padx=20, pady=5)

    password = Label(bill, text="Password", font=("Ariel", 12, "bold"))
    password.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry=Entry(bill,textvariable=user)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    passwordEntry = Entry(bill, show="*", textvariable=passs)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    btn = Button(bill, text="Login", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=adminlogin)
    btn.grid(row=5, column=1, columnspan=2)

    #btn = Button(bill, text="Customer", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
              #   command=con.contents).grid(row=7, column=2, columnspan=2)



#########################remove all widgets from screen ###############################################################
def remove_all_widgets():
    global bill
    for widget in bill.winfo_children():       #here winfo_children() collect all widgets
        widget.grid_remove()                       #this method is used for remove all widgets


####################################### Welcome user ###################################################################################
def WelcomeUser():
    remove_all_widgets()
    main_heading()
    label = Label(text="Welcome Admin ",fg="blue", bd=5, bg="sky blue", width=25, height=2,font=("Times New Roman", 12, "bold")).grid(row=1, column=1, columnspan=2)


    insert_btn = Button(bill, text="Insert", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),command=insert)
    insert_btn.grid(row=4, column=0, columnspan=2)

    update_btn = Button(bill, text="Update", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),command=update)
    update_btn.grid(row=4, column=1, columnspan=2)

    delete_btn = Button(bill, text="Delete", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),command=delete)
    delete_btn.grid(row=4, column=2, columnspan=2)


    logout()



####################################### Read Data Method through treeview ###################################################################################
def dbdataupdate():
    # fetch alla data into records
    dbrecords=displayDB.get_children()
    # to delete all the records from tree view which is already exist
    for element in dbrecords:
        displayDB.delete(element)

    # to load the table data to tree view
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="restaurant")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query="select * from data_insert"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        displayDB.insert('', 'end', text=row['ID'], values=(row["FoodItem"], row["Type"], row["Price"]))

    conn.close()
    displayDB.bind("<Double-1>",onDoubleClick)


def onDoubleClick(event):
    item=displayDB.selection()
    forKeys=displayDB.item(item,"text")   #for fetching key from database(ID)

    forValues = displayDB.item(item,"values")    #for fetching values from database(FoodItem,Type,Price)

    idItem.set(forKeys)
    foodName.set(forValues[0])
    fdTypeVar.set(forValues[1])
    rs_price.set(forValues[2])




####################################### Insert Method ###################################################################################
def insert():
    remove_all_widgets()
    main_heading()
    logout()
    backbutton()
    label = Label(text="Admin's Insert Block",fg="blue", bd=5, bg="sky blue", width=25, height=2,font=("Times New Roman", 12, "bold")).grid(row=2, column=1, columnspan=2)

    food_id = Label(bill, text="ID", font=("Ariel", 12, "bold")).grid(row=3, column=1, padx=20, pady=5)
    global idItem
    idItem = StringVar()
    id = Entry(bill,textvariable=idItem).grid(row=3, column=2, padx=20, pady=5)



    food_item = Label(bill, text="Food Item", font=("Ariel", 12, "bold")).grid(row=4, column=1, padx=20, pady=5)
    # entry1 = Entry(root).grid(row=2, column=2, padx=20, pady=5)
    global foodName
    foodName = StringVar()
    food_name = ttk.Combobox(bill, textvariable=foodName,value=["Veg Biryani", "Roti", "Green Salad", "Paneer Tikka", "Paneer DoPyaza",
                                      "Chicken Tanduri", "Half Fry", "Mutton"]).grid(row=4, column=2, padx=20, pady=5)



    food_type = Label(bill, text="Type", font=("Ariel", 12, "bold")).grid(row=5, column=1, padx=20, pady=5)
    global fdTypeVar
    fdTypeVar = StringVar()
    fdType = ttk.Combobox(bill,textvariable=fdTypeVar, value=["Breakfast","Lunch","Dinner"]).grid(row=5, column=2, padx=20, pady=5)



    price = Label(bill, text="Price", font=("Ariel", 12, "bold")).grid(row=6, column=1, padx=20, pady=5)
    global rs_price
    rs_price = IntVar()
    rs = Entry(bill, textvariable=rs_price,width=23, bd=2).grid(row=6, column=2, padx=20, pady=5)

    btn = Button(bill, text="ADD", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=msg).grid(row=7, column=1,columnspan=2, padx=20, pady=5)

    #id,food_name,quan,rs=input("Enter the values").split(",")

    ############################################Using Treeview to display database items#########################################################################

    displayDB.grid(row=8, column=0, columnspan=4)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=8, column=3, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Type")
    displayDB.heading('#3', text="Food Rate")

    dbdataupdate()


def msg():

    dbconfig()

    a = idItem.get()
    b = foodName.get()
    c = fdTypeVar.get()
    d = rs_price.get()

    insert_query = "insert into data_insert (ID, FoodItem, Type, Price) values(%s,%s,%s,%s);"
    val = (a, b, c, d)
    mycursor.execute(insert_query, val)
    print("data Inserted successfully")

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM SAVED","Item Inserted Successfully")

    #for blank the placeholder after working
    idItem.set("")
    foodName.set("")
    fdTypeVar.set("")
    rs_price.set("")

    dbdataupdate()   #for display data from database on run time


####################################### Update Method ###################################################################################
def update():
    remove_all_widgets()
    main_heading()
    logout()
    backbutton()
    label = Label(text="Admin's Update Block",fg="blue", bd=5, bg="sky blue", width=25, height=2,font=("Times New Roman", 12, "bold")).grid(row=2, column=1, columnspan=2)


    food_id = Label(bill, text="ID", font=("Ariel", 12, "bold")).grid(row=3, column=1, padx=20, pady=5)
    global idItem
    idItem = StringVar()
    id = Entry(bill, textvariable=idItem).grid(row=3, column=2, padx=20, pady=5)

    food_item = Label(bill, text="Food Item", font=("Ariel", 12, "bold")).grid(row=4, column=1, padx=20, pady=5)
    # entry1 = Entry(root).grid(row=2, column=2, padx=20, pady=5)
    global foodName
    foodName = StringVar()
    food_name = ttk.Combobox(bill, textvariable=foodName,
                             value=["Veg Biryani", "Roti", "Green Salad", "Paneer Tikka", "Paneer DoPyaza",
                                    "Chicken Tanduri", "Half Fry", "Mutton"]).grid(row=4, column=2, padx=20, pady=5)

    food_type = Label(bill, text="Type", font=("Ariel", 12, "bold")).grid(row=5, column=1, padx=20, pady=5)
    global fdTypeVar
    fdTypeVar = StringVar()
    fdType = ttk.Combobox(bill, textvariable=fdTypeVar, value=["Breakfast", "Lunch", "Dinner"]).grid(row=5, column=2,
                                                                                                     padx=20, pady=5)

    price = Label(bill, text="Price", font=("Ariel", 12, "bold")).grid(row=6, column=1, padx=20, pady=5)
    global rs_price
    rs_price = IntVar()
    rs = Entry(bill, textvariable=rs_price, width=23, bd=2).grid(row=6, column=2, padx=20, pady=5)

    btn = Button(bill, text="Update", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=updateMethod).grid(row=7, column=1, columnspan=2, padx=20, pady=5)

    displayDB.grid(row=8, column=0, columnspan=4)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=8, column=3, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Type")
    displayDB.heading('#3', text="Food Rate")

    dbdataupdate()

def updateMethod():
    dbconfig()

    idd = idItem.get()
    fn = foodName.get()
    ft = fdTypeVar.get()
    fr = rs_price.get()

    update_query = f"update data_insert set FoodItem='{fn}', Type='{ft}', Price={fr} where ID='{idd}'"
    mycursor.execute(update_query)
    print("data updated successfully")

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM SAVED", "Item Updated Successfully")

    # for blank the placeholder after working
    idItem.set("")
    foodName.set("")
    fdTypeVar.set("")
    rs_price.set("")

    dbdataupdate()  # for display data from database on run time





####################################### Delete Method ###################################################################################
def delete():
    remove_all_widgets()
    main_heading()
    logout()
    backbutton()
    label = Label(text="Admin's Delete Block",fg="blue", bd=5, bg="sky blue", width=25, height=2,font=("Times New Roman", 12, "bold")).grid(row=2, column=1, columnspan=2)


    food_id = Label(bill, text="ID", font=("Ariel", 12, "bold")).grid(row=3, column=1, padx=20, pady=5)
    global idItem
    idItem = StringVar()
    id = Entry(bill, textvariable=idItem).grid(row=3, column=2, padx=20, pady=5)

    food_item = Label(bill, text="Food Item", font=("Ariel", 12, "bold")).grid(row=4, column=1, padx=20, pady=5)
    # entry1 = Entry(root).grid(row=2, column=2, padx=20, pady=5)
    global foodName
    foodName = StringVar()
    food_name = ttk.Combobox(bill, textvariable=foodName,
                             value=["Veg Biryani", "Roti", "Green Salad", "Paneer Tikka", "Paneer DoPyaza",
                                    "Chicken Tanduri", "Half Fry", "Mutton"]).grid(row=4, column=2, padx=20, pady=5)

    food_type = Label(bill, text="Type", font=("Ariel", 12, "bold")).grid(row=5, column=1, padx=20, pady=5)
    global fdTypeVar
    fdTypeVar = StringVar()
    fdType = ttk.Combobox(bill, textvariable=fdTypeVar, value=["Breakfast", "Lunch", "Dinner"]).grid(row=5, column=2,
                                                                                                     padx=20, pady=5)

    price = Label(bill, text="Price", font=("Ariel", 12, "bold")).grid(row=6, column=1, padx=20, pady=5)
    global rs_price
    rs_price = IntVar()
    rs = Entry(bill, textvariable=rs_price, width=23, bd=2).grid(row=6, column=2, padx=20, pady=5)

    btn = Button(bill, text="Delete", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=deleteMethod).grid(row=7, column=1, columnspan=2, padx=20, pady=5)

    displayDB.grid(row=8, column=0, columnspan=4)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=8, column=3, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Type")
    displayDB.heading('#3', text="Food Rate")

    dbdataupdate()


def deleteMethod():
    dbconfig()

    idd = idItem.get()
    fn = foodName.get()
    ft = fdTypeVar.get()
    fr = rs_price.get()

    delete_query = f"delete from data_insert where ID='{idd}'"
    mycursor.execute(delete_query)
    print("data deleted successfully")

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM SAVED", "Item Deleted Successfully")

    # for blank the placeholder after working
    idItem.set("")
    foodName.set("")
    fdTypeVar.set("")
    rs_price.set("")

    dbdataupdate()  # for display data from database on run time




####################################### Logout Method ###################################################################################
def logout():
    logout_btn= Button(bill, text="LogOut", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=loginwindow)
    logout_btn.grid(row=1, column=3)
    user.set("")
    passs.set("")


####################################### Back Button###################################################################################
def backbutton():

    btn_back = Button(bill, text="Back", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                      command=WelcomeUser).grid(row=1, column=0)


####################################### Admin Login ###################################################################################
def adminlogin():
    username=user.get()
    password=passs.get()

    dbconfig()
    display = "select * from login where username='{}' and password='{}'".format(username,password)
    mycursor.execute(display)
    data=mycursor.fetchall()

    flag=False
    for row in data:
        flag = True

    conn.close()     #database connecton is close

    if flag==True:
        WelcomeUser()
    else:
        messagebox.showerror("Invalid user", "Either user name or password is incorrect")
        user.set("")
        passs.set("")




######################################## Button For First Window##############################################################
def back_4_first_window():

    btn_back1w = Button(bill, text="Back", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                      command=firstwindow).grid(row=2, column=0)

################################################# Here Customer Contents##############################################################
def Guest():
    remove_all_widgets()
    main_heading()
    back_4_first_window()
    label = Label(text="Guest Login", fg="blue", bd=5, bg="sky blue", width=25, height=2,
                  font=("Times New Roman", 12, "bold")).grid(row=1, column=1, columnspan=2)





user=StringVar()
passs=StringVar()
#main_heading()
firstwindow()
mainloop()