import pymysql

try:
    conn = pymysql.connect(host="localhost", user="root", db="pythonrain")
    mycursor = conn.cursor()
    sql_select_Query = "select * from college"

    mycursor.execute(sql_select_Query)
    records = mycursor.fetchall()
    print("Total number of rows in python_developers is - ", mycursor.rowcount)
    print("Printing each row's column values i.e.  college record")
    for row in records:
        print("Name = ", row[0] )
        print("age = ", row[1],"\n")

    mycursor.close()

except ValueError as e:
    print("Error while connecting to MySQL", e)
finally:
   conn.close()
   print("MySQL connection is closed")