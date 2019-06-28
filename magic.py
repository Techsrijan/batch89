try:
    n = int(input('Enter the number '))
    x = n
    sum , mult = 0 , 1

    while  n > 0:
        rem = n % 10
        sum = sum + rem
        mult = mult * rem
        n = n//10
    print(sum,mult)
    if sum == mult:

        print('this no. is magic number')
    else:
        print('this no. is not magic number')


except Exception as e:
    print("please enter interger number ", e)