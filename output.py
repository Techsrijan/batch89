'''i= 1
while i<=10:
    if i%4==0:
        break
    else:
        print(i)

    i= i+1'''

i= 1
while i<=10:
    i = i + 1
    if i%4==0:
        continue
    else:
        print(i)



# taking three inputs at a time
x, y, z = input("Enter a three value: ").split()
print("Total number of students: ", x)
#x=x+10
print("Number of boys is : ", y,"==",x)
print("Number of girls is : ", z)
print()



# taking three input at a time
x, y, z = [int(x) for x in input("Enter three value: ").split()]
print("First Number is: ", x)
x = x+10
print("Second Number is: ", y,x)
print("Third Number is: ", z)
print()