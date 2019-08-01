from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk



taz=Tk()
# ========mainTreeView======================
billsTV = ttk.Treeview(height=15, columns=('Rate', 'Quantity', 'Cost'))

###############database connect######################################
def dbconfig():
    global mycursor,conn
    conn=pymysql.connect(host="localhost",user="root",db="billservice")
    mycursor=conn.cursor()

###########################to create heading##########################################
def mainheading():
    head=Label(taz,text="Hotel Taz Management System",fg="green",
               bg="yellow",font=("Ariel",24,"bold"))
    head.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
#################################to create login window#####################################
def loginwindow():
    '''titleLabel = Label(taz, text="Restaurant Billing System", font="Arial 40", fg="green")
    titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))'''

    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=2, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=2, padx=20, pady=5)

    usernameEntry = Entry(taz,textvariable=usernameVar)
    usernameEntry.grid(row=2, column=3, padx=20, pady=5)

    passwordEntry = Entry(taz, show="*",textvariable=passwordVar)
    passwordEntry.grid(row=3, column=3, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2,fg="green",bd=10, command=adminlogin)
    loginButton.grid(row=4, column=2, columnspan=2)

#########################remove all widgets from screen #################

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

#########################to create welcome window ############################################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    print("hi")
    usernameLabel = Label(taz, text="Welcome User ")
    usernameLabel.grid(row=2, column=2, padx=20, pady=5)
    insertButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10, command=additem)
    insertButton.grid(row=3, column=0, padx=20, pady=5)
    searchButton = Button(taz, text="Search Item", width=20, height=2, fg="green", bd=10, command=searchitem)
    searchButton.grid(row=3, column=3, padx=20, pady=5)
    billButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10, command=billitemwindow)
    billButton.grid(row=3, column=6, padx=20, pady=5)

#######################add item window####################################
def additemwindow():
    remove_all_widgets()
    mainheading()
    additemLabel = Label(taz, text="INSERT ITEM ")
    additemLabel.grid(row=2, column=2, padx=20, pady=5)
############## get combo data ###########

def OptionCallBack(*args):
    global itemname
    itemname=variable.get()
    aa=ratelist()
    print(aa)
    global v
    for i in aa:
        for j in i:
            v=j
            print(v)
    baserate.set(aa)

def OptionCallBack1(*args):
        global qtyvalue
        quantity = qtyvariable.get()
        print(quantity)
        global costvalue
        costvalue=cost.get()


        finalvalue=int(v) * int(qtyvariable.get())


        cost.set(finalvalue)
    # print(data)
def ratelist():
    dbconfig()
    que="select rate from itemlist where name=%s"
    val=(itemname)
    mycursor.execute(que,val)

    data = mycursor.fetchall()

    return data


###################Bill Item window ##################################
def billitemwindow():
    remove_all_widgets()
    mainheading()
    additemLabel = Label(taz, text="Taz Bill Generation ")
    additemLabel.grid(row=2, column=2, padx=20, pady=5)


    billItem()

########################## bill Item ############################

def combo_input():
    dbconfig()

    mycursor.execute('SELECT name FROM itemlist')

    data = []

    for row in mycursor.fetchall():
        data.append(row[0])

    return data
variable=StringVar(taz)
qtyvariable=StringVar(taz)
baserate=StringVar()
cost=IntVar()

def billItem():
    l=combo_input()


    c = ttk.Combobox(taz,values=l,textvariable=variable)
    c.set("Select Item")
    variable.trace('w', OptionCallBack)
    c.grid(row=4, column=2, padx=20, pady=5)
    rateLabel = Label(taz, text="Rate ")
    rateLabel.grid(row=4, column=3, padx=20, pady=5)
    rateEntry =Entry(taz,textvariable=baserate)
    rateEntry.grid(row=4, column=4, padx=20, pady=5)

    quantityLabel = Label(taz, text="Quantity ")
    quantityLabel.grid(row=5, column=2, padx=20, pady=5)
    l2=[1,2,3,4,5]
    qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable)
    qty.set("Select Quantity")
    qtyvariable.trace('w', OptionCallBack1)
    qty.grid(row=5, column=3, padx=20, pady=5)

    costLabel = Label(taz, text="Cost ")
    costLabel.grid(row=6, column=1, padx=20, pady=5)
    costEntry = Entry(taz, textvariable=cost)
    costEntry.grid(row=6, column=2, padx=20, pady=5)


###################### search item window #############################
def searchitemwindow():
    remove_all_widgets()
    mainheading()
    additemLabel = Label(taz, text="Search ITEM ")
    additemLabel.grid(row=2, column=2, padx=20, pady=5)

 #################### User Search ################################
def userSearchItem():
    global search
    search=itemNameVar.get()
    dbconfig()
    query = "select * from itemlist where name like 'search%'"
    res = mycursor.execute(query)
    conn.commit()
    messagebox.showinfo("ITEM Found", "Item Found Successfully")
    conn.close()
    itemNameVar.set("")
    updateProductData()

##################### search item ##################################
def searchitem():
    searchitemwindow()

    itemNameLabel = Label(taz, text="Enter Item Name")
    itemNameLabel.grid(row=4, column=2, padx=20, pady=5)


    itemNameEntry = Entry(taz, textvariable=itemNameVar)
    itemNameEntry.grid(row=4, column=3, padx=20, pady=5)



    ItemSearchButton = Button(taz, text="Search", width=20, height=2, fg="green", bd=10, command=userSearchItem)
    ItemSearchButton.grid(row=7, column=0, columnspan=2)


    #########################################################
    productLabel = Label(taz, text="List Of Products", font="Arial 25")
    productLabel.grid(row=8, column=2)

    billsTV.grid(row=9, column=0, columnspan=5)

    scrollBar = Scrollbar(taz, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=9, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Item Id")
    billsTV.heading('#1', text="Item Name")
    billsTV.heading('#2', text="Item Rate")
    billsTV.heading('#3', text="Item Type")

    searchProductData()

################ search update treeview #################################

def searchProductData():
    # fetch alla data into records
    records = billsTV.get_children()
    # to delete all the records from tree view which is already exist
    for element in records:
        billsTV.delete(element)

    # to load the table data to tree view
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist where name like 'search%' "
    cursor.execute(query)
    data = cursor.fetchone()
    #print(data)
    for row in data:
        billsTV.insert('', 'end', text=row['nameid'], values=(row["name"], row["rate"], row["type"]))
    billsTV.bind("<Double-1>", OnDoubleClick)

    conn.close()

###################### on double click ############################


def OnDoubleClick(event):
    '''global itemNameVar
    global itemRateVar
    global ItemTypeVar
    global ItemIdVar'''
    item = billsTV.selection()
    itemIdVar1 = billsTV.item(item, "text")

    print("id=",itemIdVar)
    item_detail = billsTV.item(item, "values")
    itemIdVar.set(itemIdVar1)
    itemTypeVar.set(item_detail[2])
    itemRateVar.set(item_detail[1])
    itemNameVar.set(item_detail[0])


################# get product data from database into treeview ###########
def updateProductData():
    # fetch alla data into records
    records = billsTV.get_children()
    # to delete all the records from tree view which is already exist
    for element in records:
        billsTV.delete(element)

    # to load the table data to tree view
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist"
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    for row in data:
        billsTV.insert('', 'end', text=row['nameid'], values=(row["name"], row["rate"], row["type"]))
    billsTV.bind("<Double-1>", OnDoubleClick)

    conn.close()


##########################add item to databse ##############################
itemIdVar = StringVar()
itemNameVar = StringVar()
itemRateVar = StringVar()
itemTypeVar = StringVar()


def additem():
    additemwindow()
    '''global itemIdVar
    global itemNameVar
    global itemRateVar
    global itemTypeVar'''


    itemIdLabel = Label(taz, text="Item ID")
    itemIdLabel.grid(row=3, column=2, padx=20, pady=5)

    itemNameLabel = Label(taz, text="Item Name")
    itemNameLabel.grid(row=4, column=2, padx=20, pady=5)

    itemRateLabel = Label(taz, text="Item Rate")
    itemRateLabel.grid(row=5, column=2, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=6, column=2, padx=20, pady=5)

    itemIdEntry = Entry(taz, textvariable=itemIdVar)
    itemIdEntry.grid(row=3, column=3, padx=20, pady=5)

    itemNameEntry = Entry(taz, textvariable=itemNameVar)
    itemNameEntry.grid(row=4, column=3, padx=20, pady=5)

    itemRateEntry = Entry(taz, textvariable=itemRateVar)
    itemRateEntry.grid(row=5, column=3, padx=20, pady=5)

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=6, column=3, padx=20, pady=5)

    ItemAddButton = Button(taz, text="Add", width=20, height=2, fg="green", bd=10, command=insertItem)
    ItemAddButton.grid(row=7, column=0, columnspan=2)

    ItemDeleteButton = Button(taz, text="Delete", width=20, height=2, fg="green", bd=10, command=deleteItem)
    ItemDeleteButton.grid(row=7, column=3, columnspan=2)

    ItemUpdateButton = Button(taz, text="Update", width=20, height=2, fg="green", bd=10, command=updateItem)
    ItemUpdateButton.grid(row=7, column=6, columnspan=2)
    #########################################################
    productLabel = Label(taz, text="List Of Products", font="Arial 25")
    productLabel.grid(row=8, column=2)

    billsTV.grid(row=9, column=0, columnspan=5)

    scrollBar = Scrollbar(taz, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=9, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Item Id")
    billsTV.heading('#1', text="Item Name")
    billsTV.heading('#2', text="Item Rate")
    billsTV.heading('#3', text="Item Type")

    updateProductData()

################# update item ##############################
def updateItem():
    global itemLists
    nameid = itemIdVar.get()
    name = itemNameVar.get()
    rate = itemRateVar.get()
    type = itemTypeVar.get()
    # print(nameid,name,rate,type)

    dbconfig()
    # query = "insert into itemlist (name,nameid,rate,type) values('{}','{}','{}','{}')". format(name,nameid,rate,type)
    query = "update  itemlist set name=%s,rate=%s,type=%s where nameid=%s"
    val = (name,rate,type,nameid)
    res = mycursor.execute(query, val)
    conn.commit()
    messagebox.showinfo("ITEM Updated", "Item Updated Successfully")
    conn.close()
    itemIdVar.set("")
    itemNameVar.set("")
    itemRateVar.set("")
    itemTypeVar.set("")
    updateProductData()


###################################insert item to database####################

################delete item#################

def deleteItem():
    global itemLists
    nameid= itemIdVar.get()
    name = itemNameVar.get()
    rate = itemRateVar.get()
    type = itemTypeVar.get()
    #print(nameid,name,rate,type)



    dbconfig()
    #query = "insert into itemlist (name,nameid,rate,type) values('{}','{}','{}','{}')". format(name,nameid,rate,type)
    query="delete from itemlist where nameid=%s"
    val=(nameid)
    res=mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("ITEM Deteted","Item Deleted Successfully")
    conn.close()
    itemIdVar.set("")
    itemNameVar.set("")
    itemRateVar.set("")
    itemTypeVar.set("")
    updateProductData()
###################################insert item to database#####################

def insertItem():
    global itemLists
    nameid= itemIdVar.get()
    name = itemNameVar.get()
    rate = itemRateVar.get()
    type = itemTypeVar.get()
    #print(nameid,name,rate,type)



    dbconfig()
    #query = "insert into itemlist (name,nameid,rate,type) values('{}','{}','{}','{}')". format(name,nameid,rate,type)
    query="insert into itemlist (name,nameid,rate,type) values(%s,%s,%s,%s);"
    val=(name,nameid,rate,type)
    res=mycursor.execute(query,val)
    conn.commit()
    messagebox.showinfo("ITEM SAVED","Item Inserted Successfully")
    conn.close()
    itemIdVar.set("")
    itemNameVar.set("")
    itemRateVar.set("")
    itemTypeVar.set("")
    updateProductData()
############################to perform login operation#################################################

def adminlogin():
    username = usernameVar.get()
    password = passwordVar.get()
    dbconfig()
    query = "select * from users where username='{}' and password='{}'".format(username, password)
    mycursor.execute(query)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True

    conn.close()
    if flag==True:
        welcomewindow()

    else:
        messagebox.showerror("Invalid user", "Either user name or password is incorrect")
        usernameVar.set("")
        passwordVar.set("")


##############################################################################
taz.title("Hote1 Taz Management system")
#taz.wm_iconbitmap("notepad.ico")   #to add icon
mainheading()


usernameVar=StringVar()
passwordVar=StringVar()
loginwindow()

taz.geometry("800x600+200+100")
#taz.resizable(0,0)
mainloop()