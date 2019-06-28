try:
    n = int(input('Enter the number: '))
    x =n
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem
        n = n//10
    print('sum of',x,'=', sum)
    #print(x)



except Exception as e:
        print("please enter interger number ", e)