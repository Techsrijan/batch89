a=int(input("enter first number"))
b=int (input("enter second number"))
c=int(input("enter third number"))

print("a=",a,"b=",b,"c=",c)
print(a,b,c,sep=".....")

if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("b is greatest")
else:
    print("c is greatest")

