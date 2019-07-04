
s= 9

def msg():
    global x #how to make local varaibel to global varaible
    x=8
    print(x)

msg()
print("S=",s)

print("X=",x)