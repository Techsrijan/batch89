print("Simple Calculator")
try:
    a=int(input("Enter the First Number : "))
    b=int(input("Enter the Second Number : "))
    print("Sum = ",(a+b))
    print("Sub = ",(a-b))
    print("Mul = ",(a*b))
    print("Div = ",(a/b))
    print("ThankYou")
except Exception as e:
    print("please enter interger number ",e)
