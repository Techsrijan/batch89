from tkinter import *
import pymysql
from tkinter import messagebox,ttk,filedialog
import datetime

# from  V_FoodItem_Soft import billz
bill = Tk()
bill.title("Food Billing")
bill.geometry("805x665+280+10")
#bill.resizable(0,0)

########################## create treeview###############################################################
displayDB=ttk.Treeview(height=15, columns=('Rate', 'Quantity', 'Cost'))
displayDB1=ttk.Treeview(height=20, columns=('Rate', 'Quantity', 'Cost','dsdd', 'Qutity', 'Ct','ate', 'Quy'))
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
    searchButton = Button(bill, text="Search Item", width=20, height=2, fg="green", bd=10, command=searchitem)
    searchButton.grid(row=5, column=3, padx=20, pady=5)

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

    btnIn = Button(bill, text="ADD", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=msg).grid(row=7, column=1,columnspan=2, padx=20, pady=5)

    btnUp = Button(bill, text="Update", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=updateMethod).grid(row=7, column=0, columnspan=2, padx=20, pady=5)

    btnDl = Button(bill, text="Delete", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=deleteMethod).grid(row=7, column=3, columnspan=2, padx=20, pady=5)

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

    update_query = "update data_insert set FoodItem='{}', Type='{}', Price={} where ID='{}'".format(fn,ft,fr,idd)
    mycursor.execute(update_query)
    print("data updated successfully")

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM UPDATE", "Item Updated Successfully")

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

    confirm = messagebox.askokcancel("Alert", "Do You want to delete")
    if confirm == True:
        messagebox.showinfo("ITEM DELETE", "Item Deleted Successfully")
        delete_query = "delete from data_insert where ID='{idd}'".format(idd)
        mycursor.execute(delete_query)
        print("data deleted successfully")

    else:
        pass

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()





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








###################### search item window #############################
def searchitemwindow():
    remove_all_widgets()
    main_heading()

    additemLabel = Label(bill, text="Search ITEM ")
    additemLabel.grid(row=2, column=2, padx=20, pady=5)

 #################### User Search ################################
def userSearchItem():
    global search
    search=foodName.get()
    dbconfig()
    query = "select * from data_insert where FoodItem like 'search%' "

    res = mycursor.execute(query)
    conn.commit()
    messagebox.showinfo("ITEM Found", "Item Found Successfully")
    conn.close()
    foodName.set("")
    dbdataupdate()

##################### search item ##################################
def searchitem():
    searchitemwindow()

    itemNameLabel = Label(bill, text="Enter Item Name")
    itemNameLabel.grid(row=4, column=2, padx=20, pady=5)
    global foodName
    foodName=StringVar()
    itemNameEntry = Entry(bill, textvariable=foodName)
    itemNameEntry.grid(row=4, column=3, padx=20, pady=5)



    ItemSearchButton = Button(bill, text="Search", width=20, height=2, fg="green", bd=10, command=userSearchItem)
    ItemSearchButton.grid(row=7, column=0, columnspan=2)


    #########################################################
    productLabel = Label(bill, text="List Of Products", font="Arial 25")
    productLabel.grid(row=8, column=2)

    displayDB.grid(row=9, column=0, columnspan=5)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=9, column=4, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Rate")
    displayDB.heading('#3', text="Food Type")

    searchProductData()

################ search update treeview #################################

def searchProductData():
    # fetch alla data into records
    records = displayDB.get_children()
    # to delete all the records from tree view which is already exist
    for element in records:
        displayDB.delete(element)

    # to load the table data to tree view
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="restaurant")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from data_insert where FoodItem like 'search%' "
    cursor.execute(query)
    data = cursor.fetchone()
    #for row in data:
    displayDB.insert('', 'end', text=data['ID'], values=(data["FoodItem"], data["Type"], data["Price"]))

    conn.close()
    displayDB.bind("<Double-1>", onDouubleClick)

def onDouubleClick(event):
    item=displayDB.selection()
    forKeys=displayDB.item(item,"text")   #for fetching key from database(ID)

    forValues = displayDB.item(item,"values")    #for fetching values from database(FoodItem,Type,Price)

    idItem.set(forKeys)
    foodName.set(forValues[0])
    fdTypeVar.set(forValues[1])
    rs_price.set(forValues[2])























################################################# Here Customer Contents##############################################################
def Guest():
    remove_all_widgets()
    main_heading()
    back_4_first_window()

    btn_order = Button(bill, text="BillGenerate", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                        command=billItem).grid(row=2, column=1)

    btn_billGenerate = Button(bill, text="Order", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                       command=customerOrder).grid(row=2, column=2)

    label = Label(text="Guest Login", fg="blue", bd=5, bg="sky blue", width=25, height=2,
                  font=("Times New Roman", 12, "bold")).grid(row=1, column=1, columnspan=2)
    lbl=Label(text="").grid(row=3,column=0)
    """displayDB.grid(row=8, column=0, columnspan=4)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=8, column=3, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Type")
    displayDB.heading('#3', text="Food Rate")

    dbdataupdate()"""





################################################# Here Customer order##############################################################

def customerOrder():
    remove_all_widgets()
    main_heading()
    logout()
    back_4_customer_window()
    label = Label(text="Customer Order Block", fg="blue", bd=5, bg="sky blue", width=25, height=2,
                  font=("Times New Roman", 12, "bold")).grid(row=2, column=1, columnspan=2)

    food_id = Label(bill, text="ID", font=("Ariel", 12, "bold")).grid(row=3, column=1, padx=20, pady=5)
    global idItem
    idItem = StringVar()
    id = Entry(bill, textvariable=idItem).grid(row=3, column=2, padx=20, pady=5)

    food_item = Label(bill, text="Food Item", font=("Ariel", 12, "bold")).grid(row=4, column=1, padx=20, pady=5)
    # entry1 = Entry(root).grid(row=2, column=2, padx=20, pady=5)
    global foodName
    foodName = StringVar()
    food_name = ttk.Combobox(bill, textvariable=foodName, value=["Veg Biryani", "Roti", "Green Salad", "Paneer Tikka", "Paneer DoPyaza",
                                    "Chicken Tanduri", "Half Fry", "Mutton"]).grid(row=4, column=2, padx=20, pady=5)

    food_type = Label(bill, text="Type", font=("Ariel", 12, "bold")).grid(row=5, column=1, padx=20, pady=5)
    global fdTypeVar
    fdTypeVar = StringVar()
    fdType = ttk.Combobox(bill, textvariable=fdTypeVar, value=["Breakfast", "Lunch", "Dinner"]).grid(row=5, column=2,padx=20, pady=5)


    quantity = Label(bill, text="Quantity", font=("Ariel", 12, "bold")).grid(row=6, column=1, padx=20, pady=5)
    global amount
    amount = IntVar()
    num = ttk.Combobox(bill, value=list(range(1, 10)), textvariable=amount).grid(row=6, column=2, padx=20, pady=5)



    price = Label(bill, text="Price", font=("Ariel", 12, "bold")).grid(row=7, column=1, padx=20, pady=5)
    global rs_price
    rs_price = IntVar()
    rs = Entry(bill, textvariable=rs_price, width=23, bd=2).grid(row=7, column=2, padx=20, pady=5)

    btn = Button(bill, text="Order", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=msges).grid(row=8, column=1, columnspan=2, padx=20, pady=5)

    # id,food_name,quan,rs=input("Enter the values").split(",")

    ############################################Using Treeview to display database items#########################################################################

    displayDB.grid(row=9, column=0, columnspan=4)

    scrollBar = Scrollbar(bill, orient="vertical", command=displayDB.yview)
    scrollBar.grid(row=9, column=3, sticky="NSE")

    displayDB.configure(yscrollcommand=scrollBar.set)

    displayDB.heading('#0', text="Food Id")
    displayDB.heading('#1', text="Food Name")
    displayDB.heading('#2', text="Food Type")
    displayDB.heading('#3', text="Food Rate")

    dbdataupdate()

def msges():

    dbconfig()

    a = idItem.get()
    b = foodName.get()
    c = fdTypeVar.get()
    d = amount.get()
    e = rs_price.get()

    insert_query = "insert into guest_order (ID, FoodItem, Type,Quantity, Price) values(%s,%s,%s,%s,%s);"
    val = (a, b, c, d,e)
    mycursor.execute(insert_query, val)
    print("Order successfully")

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM SAVED","Your Food Ordered Successfully")

    #for blank the placeholder after working
    #idItem.set("")
    foodName.set("")
    fdTypeVar.set("")
    amount.set("")
    rs_price.set("")

    dbdataupdate()   #for display data from database on run time

######################################## Button For First Window##############################################################
def back_4_customer_window():

    btn_back1w = Button(bill, text="Back", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                      command=Guest).grid(row=1, column=0)




######################################## Combo BOX Button For  Generating Bill##############################################################

def OptionCallBack(*args):
    global itemname,aa
    itemname=variable.get()
    aa=ratelist()
    print("Aa isv = ",aa)
    baserate.set(aa)
    print(aa)
    global vii
    for i in aa:
        for j in i:
        #cc=int(i)

            vii=j
            print(type(vii))

def OptionCallBack1(*args):
    global qty
    qty = quan.get()
    print(qty)
    global costvalue
    costvalue = getbill.get()

    finalvalue = int(vii) * quan.get()
    getbill.set(finalvalue)

    gst = (finalvalue * 18)/100
    taxbill.set(gst)

    totalbill=finalvalue + gst
    total.set(totalbill)






    # print(data)
def ratelist():
    dbconfig()
    que="select Price from data_insert  where FoodItem=%s"
    val=(itemname)
    mycursor.execute(que,val)

    data = mycursor.fetchall()

    return data


###################Bill Item window ##################################


########################## bill Item ############################

def combo_input():
    dbconfig()

    mycursor.execute('SELECT FoodItem FROM data_insert')

    data = []

    for row in mycursor.fetchall():
        data.append(row[0])

    return data
variable=StringVar(bill)

baserate=IntVar()
#################################### Validation ##############################
def only_Alpha(P):
    if P.isalpha() or P=="":
        return True
    return False

def billItem():
    remove_all_widgets()
    main_heading()
    additemLabel = Label(bill, text="Bill Generation Block", fg="blue", bd=5, bg="sky blue", width=25, height=2,
                         font=("Times New Roman", 12, "bold"))
    additemLabel.grid(row=1, column=1, padx=20, pady=5, columnspan=2)

    btn_back1w = Button(bill, text="Back", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                        command=Guest)

    btn_back1w.grid(row=1, column=0)
    l=combo_input()

    #lbl=Label(bill,text="").grid(row=2, column=1)

    td = Label(bill, text="Time/Date", font=("Ariel", 12, "bold")).grid(row=3, column=0, padx=20, pady=5)
    global x
    x = datetime.datetime.now()
    global timedate
    timedate = StringVar()
    id1 = Entry(bill, textvariable=timedate).grid(row=3, column=1, padx=20, pady=5)
    timedate.set(x)

    lbl = Label(bill, text="").grid(row=4, column=1)
    customerName = Label(bill, text="Customer Name", font=("Ariel", 12, "bold")).grid(row=5, column=0, padx=20, pady=5)


    global guestName
    guestName = StringVar()
    GuestNaam = Entry(bill, textvariable=guestName)
    GuestNaam.grid(row=5, column=1, padx=20, pady=5)
    callback = bill.register(only_Alpha)  # registers a Tcl to Python callback
    GuestNaam.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    lbl = Label(bill, text="").grid(row=6, column=1)
    mob = Label(bill, text="Mobile", font=("Ariel", 12, "bold")).grid(row=7, column=0, padx=20, pady=5)
    global mobile
    mobile = IntVar()
    id3 = Entry(bill, textvariable=mobile).grid(row=7, column=1, padx=20, pady=5)

    lbl = Label(bill, text="").grid(row=8, column=1)
    email = Label(bill, text="E-mail", font=("Ariel", 12, "bold")).grid(row=9, column=0, padx=20, pady=5)
    global mail
    mail = StringVar()
    id4 = Entry(bill, textvariable=mail).grid(row=9, column=1, padx=20, pady=5)


    c_lbl = Label(bill, text="Selcet Your FooD",font=("Times New Roman", 12, "bold")).grid(row=3, column=2)
    c = ttk.Combobox(bill,values=l,textvariable=variable)
    c.set("Select Item")
    variable.trace('w', OptionCallBack)
    c.grid(row=3, column=3)

    lbl = Label(bill, text="").grid(row=4, column=1)

    rateLabel = Label(bill, text="Rate ", font=("Times New Roman", 12, "bold"))
    rateLabel.grid(row=5, column=2)
    rateEntry =Entry(bill,textvariable=baserate)
    #print(baserate)
    rateEntry.grid(row=5, column=3)

    lbl = Label(bill, text="").grid(row=6, column=1)

    quantity = Label(bill, text="Quantity", font=("Ariel", 12, "bold")).grid(row=7, column=2)
    global quan
    quan = IntVar()
    quanEntry = ttk.Combobox(bill, value=list(range(1, 10)), textvariable=quan)
    quanEntry.set("Select Quantity")
    quan.trace('w', OptionCallBack1)
    quanEntry.grid(row=7, column=3, padx=20, pady=5)

    #print(quanEntry)

    lbl = Label(bill, text="").grid(row=8, column=1)
    b = Label(bill, text="Bill", font=("Ariel", 12, "bold")).grid(row=9, column=2, padx=20, pady=5)
    global getbill
    getbill = IntVar()
    id5 = Entry(bill, textvariable=getbill).grid(row=9, column=3, padx=20, pady=5)

    lbl = Label(bill, text="").grid(row=10, column=1)
    bc = Label(bill, text="18% GST", font=("Ariel", 12, "bold")).grid(row=11, column=2, padx=20, pady=5)
    global taxbill
    taxbill = IntVar()
    id6 = Entry(bill, textvariable=taxbill).grid(row=11, column=3, padx=20, pady=5)

    lbl = Label(bill, text="").grid(row=12, column=1)
    tatal = Label(bill, text="Total Payable amount", font=("Ariel", 12, "bold")).grid(row=13, column=2, padx=20, pady=5)
    global total
    total = IntVar()
    id7 = Entry(bill, textvariable=total).grid(row=13, column=3, padx=20, pady=5)


    btnBill = Button(bill, text="BILL", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                 command=insertorder).grid(row=14, column=1, columnspan=2, padx=20, pady=5)


def insertorder():

    dbconfig()
    global a
    a = timedate.get()
    b = guestName.get()
    c = mobile.get()
    d = mail.get()
    e = variable.get()
    f = vii
    g = quan.get()
    h = getbill.get()
    i=  taxbill.get()
    j= total.get()

    insert_query = "insert into guest_bill (TimeAndDate, Name, Mobile, Email,FoodName,Rate, Quantity, Bill, GST, TotalAmount) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    val = ( a,b, c, d,e,f,g,h,i,j)
    mycursor.execute(insert_query, val)
    print("data Ordered successfully")
    finallybill()

    # data = mycursor.fetchall()

    conn.commit()
    conn.close()
    messagebox.showinfo("ITEM SAVED","Item Ordered Successfully")
    finallybill()
    #for blank the placeholder after working
    """idItem.set("")
    foodName.set("")
    fdTypeVar.set("")
    rs_price.set("")"""






def finallybill():
    remove_all_widgets()
    main_heading()
    back_btnBill = Button(bill, text="BACK", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                     command=billItem).grid(row=1, column=0, columnspan=2, padx=20, pady=5)

    back_btnBill = Button(bill, text="Reciept", bg="pink", justify="center", bd=2, font=("Ariel", 12, "bold"),
                          command=reciept).grid(row=1, column=2, columnspan=2, padx=20, pady=5)

    #displayDB.configure(yscrollcommand=scrollBar.set)
    displayDB1.grid(row=2, column=0,columnspan=8)

    displayDB1.heading('#0', text="Date/Time")
    displayDB1.heading('#1', text="Name")
    displayDB1.heading('#2', text="Mobile")
    displayDB1.heading('#3', text="Selected Food")
    displayDB1.heading('#4', text="Rate")
    displayDB1.heading('#5', text="Quantity")
    displayDB1.heading('#6', text="Total Amount")
    displayBill()

##################################################### Updating The CUstomer Bill##########################
def displayBill():
    # fetch all data into records
    dbrecords=displayDB1.get_children()
    # to delete all the records from tree view which is already exist
    for element in dbrecords:
        displayDB1.delete(element)

    # to load the table data to tree view
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="restaurant")
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    query="select * from guest_bill WHERE TimeAndDate='{}';".format(a)
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        displayDB1.insert('', 'end', text=row['TimeAndDate'], values=(row["Name"], row["Mobile"],row["FoodName"], row["Rate"], row["Quantity"], row["TotalAmount"]))

    conn.close()


    """displayDB.bind("<Double-1>",onDoubleClick)


def onDoubleClick(event):
    item=displayDB.selection()
    forKeys=displayDB.item(item,"text")   #for fetching key from database(ID)

    forValues = displayDB.item(item,"values")    #for fetching values from database(FoodItem,Type,Price)

    idItem.set(forKeys)
    foodName.set(forValues[0])
    fdTypeVar.set(forValues[1])
    rs_price.set(forValues[2])"""


def reciept():
    global itemLists
    global totalCost

    billString = ""
    billString += "=====================Receipt==========================\n\n"
    billString += "======================================================\n"
    billString += "{:<20}{:<10}{:<15}{:<10}\ns".format("Name", "Rate", "Quantity", "Total Amount")
    billString += "======================================================\n"

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="restaurant")
    cursor = conn.cursor()

    query = "select * from guest_bill WHERE TimeAndDate='{}';".format(a)
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)

    for row in data:
        #billString.insert('', 'end', text=row['TimeAndDate'], values=(row["Name"], row["Mobile"],row["FoodName"], row["Rate"], row["Quantity"], row["TotalAmount"]))
        print("Time and date = ",row[0])
        print("Name = ",row[1])
        print("Mobile = ",row[2])
        print("Food NAme = ",row[3])
        print("Rate = ",row[4])

        billString += "{:<20}{:<10}{:<15}{:<10}\n".format(row[0], row[1], row[2], row[3])

        billString += "======================================================\n"
        billString += "{}{:<10}{:<15}{:<10}\n".format("Total Cost", " ", " ", row[9])


    billFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if billFile is None:
        messagebox.showerror("Invalid file Name", "Please enter valid name")
    else:
        billFile.write(billString)
        billFile.close()

    print(billString)

    itemLists = []
    totalCost = 0.0
    # updateListView()
    # totalCostVar.set("Total Cost = {}".format(totalCost))"""





#################################### Validation ##############################
"""def only_Alpha(P):
    if P.isalpha() or P=="":
        return True
    return False"""





user=StringVar()
passs=StringVar()
#main_heading()
firstwindow()
mainloop()