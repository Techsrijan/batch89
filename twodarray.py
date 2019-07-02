from numpy import *

arr= array([

    [1,2,3,4],
    [6,7,8,9]
])


print(arr)

print(arr.dtype)

print(arr.ndim)

print(arr.shape)

print(arr.size)

arr2= arr.flatten()
print(arr2)

arr3 = arr2.reshape(4,2)
print(arr3)





