'''import array
import array as arr'''
import time
from array import  *


marks1=array('i',[4,5,6,3,23,55])
print(marks1)

marks=array('f',[4,5,6,3,23,55.5])
print(marks)

print(marks.buffer_info())

print(marks.typecode)

for i in range(len(marks)):
    print(marks[i],end="")

print()
for i in range(6):
    time.sleep(1)
    print(marks[i])

print("another way")
for data in marks:
    print(data,"\t",end="")

print()
name= array('u',['a','b','c','d'])
print(name)

i=0
while i<len(name):
    print(name[i])
    i=i+1

