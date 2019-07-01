from math import *
try:
    n = int(input("Enter the number : "))
    num = n
    sum = 0
    while n > 0:
        sum += pow(n%10,3)
        n = n//10

    print("Sum is :",sum)
    if num == sum:
        print(num, "is a Palindrome number.")
    else:
        print(num, "is not a Palindrome number.")

except Exception as e:
    print("You cannot enter the invalid input \nThe error is :",e)

