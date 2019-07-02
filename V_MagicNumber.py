try:
    n = int(input("Enter the number : "))
    num = n
    sum = 0
    prod = 1
    while n > 0:
        sum += n%10
        prod *= n%10
        n = n//10

    print("Sum is :",sum)
    print("Product is : ",prod)
    if sum == prod:
        print(sum,"and",prod,"are equal number.","So,",num,"is a Magic number")
    else:
        print(sum,"and",prod,"are not equal number.","So,",num,"is not a Magic number")

except Exception as e:
    print("You cannot enter the invalid input \n The error is :", e)

