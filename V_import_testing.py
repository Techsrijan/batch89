from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import filedialog, colorchooser
from tkinter import ttk
window=Tk()

###############database connect######################################
def dbconfig():
    global mycursor,conn
    conn=pymysql.connect(host="localhost",user="root",db="billservice")
    mycursor=conn.cursor()

###########################to create heading##########################################

# ========mainTreeView======================
billsTV = ttk.Treeview(height=15, columns=('Item Name''Rate', 'Quantity', 'Cost'))

window.title("Hote1 Taz Management system")

def updateItem():
    global addItemRateVar
    global addQuantityVar
    global updateItemName

    name = updateItemName.get()
    rate = addItemRateVar.get()
    quantity = addQuantityVar.get()

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor()
    query = "update  bill set rate='{}',quantity='{}' where name='{}'".format(rate,quantity,name)

    cursor.execute(query)
    conn.commit()
    conn.close()

    updateItemName.set("")
    addItemRateVar.set("")
    addQuantityVar.set("")
    updateBillsData()

def OnDoubleClick(event):
    global addItemRateVar
    global addQuantityVar
    global updateItemName
    item = billsTV.selection()
    updateItemName = billsTV.item(item, "text")
    item_detail = billsTV.item(item, "values")

    '''addItemRateVar.set(item_detail[1])
    addQuantityVar.set(item_detail[2])'''





# =================update bill data===========
def updateBillsData():
    records = billsTV.get_children()

    for element in records:
        billsTV.delete(element)

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="billservice")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    #cursor = conn.cursor()
    query = "select * from bill"
    cursor.execute(query)
    data = cursor.fetchall()
    #print(data)
    for row in data:
        billsTV.insert('', 'end', text=row['name'], values=(row["rate"], row["quantity"], row["cost"]))

    billsTV.bind("<Double-1>", OnDoubleClick)
    conn.close()



def viewAllBills():
    mainwindow()
    #backButton = Button(window, text="Back", command=lambda: readAllData())
   # backButton.grid(row=0, column=1)
    '''titleLabel = Label(window, text="Taz Billing System", width=40, font="Arial 30", fg="green")
    titleLabel.grid(row=0, column=2, columnspan=4, pady=(10, 0))'''
    billsTV.grid(row=4, column=0, columnspan=5)

    scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
    scrollBar.grid(row=4, column=4, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Item Name")
    billsTV.heading('#1', text="Rate")
    billsTV.heading('#2', text="Quantity")
    billsTV.heading('#3', text="Cost")

    updateBillsData()

################ print bill###################

def print_bill():
    global itemLists
    global totalCost

    billString = ""
    billString += "=====================Receipt==========================\n\n"
    billString += "======================================================\n"
    billString += "{:<20}{:<10}{:<15}{:<10}\ns".format("Name", "Rate", "Quantity", "Cost")
    billString += "======================================================\n"

    for item in itemLists:
        billString += "{:<20}{:<10}{:<15}{:<10}\n".format(item["name"], item["rate"], item["quantity"], item["cost"])

    billString += "======================================================\n"
    billString += "{:<20}{:<10}{:<15}{:<10}\n".format("Total Cost", " ", " ", totalCost)

    billFile = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if billFile is None:
        messagebox.showerror("Invalid file Name", "Please enter valid name")
    else:
        billFile.write(billString)
        billFile.close()

    print(billString)

    itemLists = []
    totalCost = 0.0
    #updateListView()
    #totalCostVar.set("Total Cost = {}".format(totalCost))

def mainwindow():



    updateItem = Button(window, text="Update Item", width=15, height=2)
    updateItem.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

    rateLabel = Label(window, text="Rate")
    rateLabel.grid(row=2, column=0, padx=(10, 0), pady=(10, 0))


    costEntry = Entry(window, textvariable="addItemRateVar")
    costEntry.grid(row=2, column=1, padx=(10, 0), pady=(10, 0))

    quantityLabel = Label(window, text="Quantity")
    quantityLabel.grid(row=3, column=0, padx=(5, 0), pady=(10, 0))
    quantityEntry = Entry(window, textvariable="addQuantityVar")
    quantityEntry.grid(row=3, column=1, padx=(5, 0), pady=(10, 0))





viewAllBills()
window.geometry("800x600+200+100")
window.resizable(0,0)
mainloop()