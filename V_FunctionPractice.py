#1 Factorial Program
"""def fact(num):
    i = 1
    f = 1
    while i <= num:
        f = f * i
        i = i + 1
    return f


n = int(input("Enter any number : "))
a = fact(n)
print("Factorial of", n, "is :", a)"""





#2 Prime No.
"""def prime(num):
    i = 1
    k = 0
    while i <= num:
        if num % i == 0:
            k = k + 1
        i = i + 1
    return k

n = int(input("Enter any number : "))
a = prime(n)


if a == 2:
    print(n,": is a Prime Number ")
else:
    print(n,": is not a Prime Number ")"""






#3 sum of all numbers in list
"""
def addlist(lst):
    a = sum(lst)
    return a

l=[5,4,6,3,8]
s= addlist(l)
print("Sum of all no. in list =",s)"""







# multiply of all numbers in list
"""def prodlist(l):
    prod = 1
    for i in l:
        prod *=i
    return prod
a=[5,4,6,3,8]
p= prodlist(a)
print("Sum of all no. in list =",p)"""




# reverse a string
"""def revstring(string):
    rev = string[-1::-1]
    return rev

name = input("Enter the string : ")
print("Reverse of",name,"is :",revstring(name))"""







#8 print unique value from list

"""def uniquelist(l):
    return list(set(l))

lst = [1,22,3,22,33,4,3,4,1,33,22,6,8,6]
print("Unique List is :",uniquelist(lst))"""





#10 print only even values in the list

"""def evenlist(l):
    x = []
    for i in l:
        if i % 2 == 0:
            x.append(i)
    return x

lst = [1,22,3,22,33,4,3,4,1,33,22,6,8,6]
print("Only Even no. is :",evenlist(lst))"""


#12 check pass string is palindrome or not

"""def checkPalindrome(string):
    x = string[-1::-1]
    if string == x:
        return "String is Palindrome !!"
    else:
        return "String is not Palindrome !!"

c = input("Enter the String : ")
checkPalindrome(c)
print(checkPalindrome(c))"""







#print Square of every values in list
"""def squarelist(l):
    x = []
    for i in l:
        x.append(i**2)
    return x

#lst = [1,2,3,4,5,6,7,8,9,10]
lst = list(range(1,21))
print(lst)
print("Square of every values in list :",squarelist(lst))"""


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def calstring(name):
    capital=small=space = 0
    for i in name:
        if i.isupper():
            capital += 1
        elif i.islower():
            small += 1
        elif i == " ":
            space += 1
        else:
            pass
    return capital,small,space

username = input("Enter your Sentence : ")
C,s,sp=calstring(username)
print("No. of Capital letters is : {}\nNo. of small letters is : {}\nNo. of total spaces is : {}".format(C,s,sp))


#GCD program

"""def gcd(n1,n2):
    x = []
    y = []

    for i in range(1,n1+1):
        if n1 % i == 0:
            x.append(i)

    for j in range(1,n2+1):
        if n2 % j == 0:
            y.append(j)

    return x,y

#a = int(input("Enter first no. : "))
#b = int(input("Enter second no. : "))
a,b = [int(k) for k in input("Enter your numbers : ").split(",")]
m,n=gcd(a,b)

print("Factors of ",a,"is :",m,"\nFactors of ",b,"is :",n)

if max(m) in n:
    print("GCD is = ",max(m))
elif max(n) in m:
    print("GCD of",a,"and",b," = ", max(n))


else:
    print("GCD is not posssible ")"""

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

