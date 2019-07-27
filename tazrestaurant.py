from tkinter import *
from tkinter import messagebox
import pymysql


taz=Tk()

###############database connect######################################
def dbconfig():
    global mycursor,conn
    conn=pymysql.connect(host="localhost",user="root",db="billservice")
    mycursor=conn.cursor()

###########################to create heading##########################################
def mainheading():
    head=Label(taz,text="Hotel Taz Management system",fg="green",
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


##############################################################################
taz.title("Hote1 Taz Management system")
mainheading()
usernameVar=StringVar()
passwordVar=StringVar()
loginwindow()

taz.geometry("700x600+200+100")
taz.resizable(0,0)
mainloop()