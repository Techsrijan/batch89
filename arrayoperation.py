from numpy import *
import os
import time
arr = array([1,12,33,4,5])
print(arr)

arr = arr + 5

print(arr)

arr2 =ones(5)
print(arr2)



arr3 = arr + arr2
print(arr3)


'''for i in arr3:
    time.sleep(1)
    print(i)'''

arr4 = sqrt(arr)
print(arr4)

print("Min=",min(arr))

print("Max=",max(arr))

print("Sum=",sum(arr))

a = sort(arr)
print(a)


print(concatenate([arr,arr2]))

print(concatenate([arr2,arr]))

s=char.array(['ram','shyam'])
s1=char.array(['Sharma','singh'])

print(s)
print(s1)

s3= s+s1
print(s3)




