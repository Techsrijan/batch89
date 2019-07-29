import pymysql

conn=pymysql.connect(host="localhost",user="root", db="hostel")
mycursor=conn.cursor()
print("OK")

#que="create table college  (Name varchar(25), age int(3))"
#mycursor.execute(que)
#print("done table created")



#queinsert="insert into college(Name,age) values('ram',25);"
#mycursor.execute(queinsert)

"""name,age=input("Enter values").split(",")
queinsert="insert into college(Name,age) values(%s,%s);"
val=(name,age)
mycursor.execute(queinsert,val)"""

updateins="update college set age=60 where Name='Ibane'"
mycursor.execute(updateins)
conn.commit() #this line is used for save our query VV Im
print("Value Inserted Succesfully")



conn.close()
