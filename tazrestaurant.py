from tkinter import *
from tkinter import messagebox
import pymysql


taz=Tk()
global itemIdVar
global itemNameVar
global itemRateVar
global itemTypeVar
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


###################################insert item to database#####################
def insertItem():
    pass


#######################add item window####################################
def additemwindow():
    remove_all_widgets()
    mainheading()
    additemLabel = Label(taz, text="INSERT ITEM ")
    additemLabel.grid(row=2, column=2, padx=20, pady=5)

##########################add item to databse ##############################
def additem():
    additemwindow()

    itemIdVar = StringVar()
    itemNameVar = StringVar()
    itemRateVar = StringVar()
    itemTypeVar = StringVar()

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
    ItemAddButton.grid(row=7, column=2, columnspan=2)


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
        usernameVar.set=""


##############################################################################
taz.title("Hote1 Taz Management system")
mainheading()


usernameVar=StringVar()
passwordVar=StringVar()
loginwindow()

taz.geometry("700x600+200+100")
taz.resizable(0,0)
mainloop()