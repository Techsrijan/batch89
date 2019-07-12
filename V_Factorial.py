try:
    n = int(input("Enter any number : "))
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i

        if i == 1:
            print(i,"=",fact)
        else:
            print(i,"* ",end="")

    print()
    print("Factorial of",n, "=",fact)

except Exception as e:
    print("You cannot enter the invalid input \nThe error is :",e)
