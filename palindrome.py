try:
    n = int(input('Enter the number '))
    x = n
    dig = 0
    while  n > 0:
        rem = n % 10
        dig = dig*10+rem
        n = n // 10

    if x == dig:
        print('the number is a Palindrome...')
    else:
        print('the number is not a Palindrome...')

except Exception as e:
    print("please enter interger number ", e)