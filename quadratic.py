'''

a x*x+b*x+c=0
has 2 roots

d= b**b-4*a*c
x1,x2=(-b+-sqrt(d))/(2*a)


if d==0
real
   equal
x1=x2=-b/(2*a)
elif d>0
x1
x2
else



   unequal
imaginary

'''
from math import *
a=int(input("enter first number"))
b=int (input("enter second number"))
c=int(input("enter third number"))

print("a=",a,"b=",b,"c=",c)

d= b*b-4*a*c

if d==0:
    x1 = x2 = -b / (2 * a)
    print("X1=",x1,"X2=",x2)
elif d>0:
    x1 = -b - sqrt(d) / (2 * a)
    x2 = -b + sqrt(d) / (2 * a)
    print("X1=", x1, "X2=", x2)
    print("x1=", format(x1,".2f"))
else:
    print("Roots are imaginary")

