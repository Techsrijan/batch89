from numpy import *

arr= array([

    [1,2,3,4],
    [6,7,8,9],
    [23,44,55,76],
    [62,73,84,96]
])

arr2= array([

    [1,1,1,1],
    [1,1,1,1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
])

#print(arr)

a= matrix(arr)
b= matrix(arr2)
print("matrix a")
print(a)
print("matrix b")
print(b)
print("add a and b")
c = a+b
print(c)

print("Multi a and B")
d= a*b
print(d)

print("Matrix diogonal element")
print(diagonal(a))


print(linalg.inv(a))