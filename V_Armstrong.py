try:
    n = int(input("Enter the number : "))
    num = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n%10
        n = n//10

    if rev == num:
        print(num,"is Armstrong number.")
    else:
        print(num,"is not a Armstrong number.")

except Exception as e:
    print("You cannot enter the invalid input \nThe error is :",e)



# For srting

"""name = input("Enter a string :")
rev=name[-1::-1]
if name == rev:
    print(name,"is Armstrong.")
else:
    print(name,"is not Armstrong.")"""