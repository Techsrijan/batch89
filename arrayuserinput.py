from array import  *
n =  int(input("how may students u have?"))
print("no of students=",n)
marks =array('i',[])
for i in range(n):
    x= int(input("Enter the marks of student"))
    marks.append(x)

print(marks)
search = int(input("Enter the marks u want search"))
k=0
for a in marks:
    if a==search:
        print("Mil gaya",k+1)
        break
    k=k+1

else:print("Nahi mila")

print("by using array funcion")
print(marks.index(search))