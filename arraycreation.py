from numpy import *
'''
There are six ways to create an array using numpy

1.by auging array()
2. linspace
3.logspace
4.arange
5.zeros
6.ones
'''

arr = array([1,2,3,45,6])
print(arr)

arr2= linspace(0,15)
print(arr2)

arr3= linspace(0,15,14)
print(arr3)


arr4= logspace(0,15,5)
print(arr4)

arr5= array([0,0,0,0,0,0,0,])
print(arr5)

arr6 =zeros(10)
print(arr6)

arr7 =ones(10)
print(arr7)

arr8=arange(1,15,2)
print(arr8)


