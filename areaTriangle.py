# import math
from math import sqrt
try:
    a = float(input("Enter first side of Triangle : "))
    b = float(input("Enter second side of Triangle : "))
    c = float(input("Enter third side of Triangle : "))
    s = a+b+c
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of Triangle = ", area)
except Exception as e:
    print("please enter interger number ",e)
