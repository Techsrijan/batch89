try:
    n = int(input("Enter the number : "))
    num = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n%10
        n = n // 10
    print("Reverse of ", num, "is :", rev)

except Exception as e:
    print("You cannot enter the invalid input \n The error is :",e)




