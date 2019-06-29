try:
    evensum = 0
    oddsum = 0
    for i in range(1,101):
        if i % 2 == 0:
            evensum += i
        else:
            oddsum += i
    else:
        print("Sum of all even numbers between 1 to 100 : ", evensum)
        print("Sum of all odd numbers between 1 to 100 : ", oddsum)

except Exception as e:
    print("You cannot enter the invalid input \nThe error is :",e)

