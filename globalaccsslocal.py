s= 9
x=20
print(id(x))
def msg():
    # what if u want to print global varaible here
    a=globals()['x'] # it will acess global varaible
    x=55
    print(x)
    print("inside=",id(x))
    print("Inside msg function=",a)


msg()
print("S=",s)

print("X=",x)