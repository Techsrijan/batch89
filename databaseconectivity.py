import pymysql

conn=pymysql.connect(host="localhost",user="root",db="pythonrain")
mycursor=conn.cursor()
print("Connection established")
'''que="create table college (Name varchar(25), age int(3))"
mycursor.execute(que)
print("table created successfully")
name,age=input("enter name and age").split()
print(name,age)
#queins="insert into college(Name,age) values('ram',25)"
queins="insert into college(Name,age) values(%s,%s);"
val=(name,age)
mycursor.execute(queins,val)
updateins="update college set age=60 where Name='abcd'"
mycursor.execute(updateins)'''

que="select * from college"
res=mycursor.execute(que)
for row in res:
    print(row[0])
print(res)
conn.commit()
print("data inserted successfully")
conn.close()