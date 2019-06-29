try:
    n = int(input("Enter any number : "))
    sum = 0
    while n > 0:
        sum += n%10
        n = n//10
    else:
         print("Sum of all digits is : ",sum)

except Exception as e:
    print("You cannot enter the invalid input \nThe error is :",e)


#Using String Way
print("\nUsing String Way")
n=input("Enter the number : ")
sum = 0
for i in n:
    sum += int(i)
print("Sum of all digits is : ",sum)
