try:
    n = int(input("Enter the no. : "))
    x=n
    sum = 0
    while n > 0:
        rem = n % 10
        rem = rem**3
        sum = sum + rem
        n = n//10
    if x == sum:
        print('number is Armstrong number')
    else:
        print('number is not Armstrong number')


except Exception as e:
    print("please enter interger number ",e)