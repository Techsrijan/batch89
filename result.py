a = int(input("Enter the marks of first Subject : "))
b = int(input("Enter the marks of second Subject : "))
c = int(input("Enter the marks of third Subject : "))
d = int(input("Enter the marks of fourth Subject : "))
e = int(input("Enter the marks of fifth Subject : "))
tot = a + b + c + d + e
per = (tot*100)/500
print("You got = ", per,"%")
if per < 33:
    print("You are fail")
elif per >=33 and per <45:
    print("Third Division Passed")
elif per >=45 and per <60:
    print("Second Division Passed")
else:
    print("First Division Passed")

