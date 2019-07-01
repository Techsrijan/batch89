from numpy import *

arr = array([1,12,33,4,5])
print(arr)

# aliasing an array
arr2 = arr

print(arr2)

print(id(arr))
print(id(arr2))

# what if u want diffrent address
# shallow copy
arr3 = arr.view()

print(arr3)
print("view")
print(id(arr))
print(id(arr3))

print(arr[1])

print(arr)
arr[1]=5000

print(arr)
print(arr3)


# what if u want different address as well as does not effect with each other

#deep copy
arrdeep=arr.copy()
print(arrdeep)
print("deep")
print(id(arr))
print(id(arrdeep))
arr[3]=5000

print(arr)
print(arrdeep)