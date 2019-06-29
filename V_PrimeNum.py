"""n=int(input("Enter any number : "))
i=1
k=0

while i<=n:
    if n % i == 0:
        k = k+1
    i = i + 1
else:
    if k == 2:
        print(n,"is a prime number.")
    else:
        print(n,"is not a prime number.")"""



import time
#n=int(input("Enter any number : "))
print("Prime numbers between 1 to 10")
n=1
while n <= 10:
    i=1
    k=0
    while i<=n:
        if n % i == 0:
            k = k + 1
        i = i + 1
    else:
        if k == 2:
            time.sleep(1)
            print(n, " is a prime number.")

    n = n + 1







