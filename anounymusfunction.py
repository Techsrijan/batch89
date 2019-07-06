from functools import *

def add(a,b):
    return a+b

'''
lambda function--function without name
can accept any number of argument but have only one expression
'''

print(add(5,6))

f=lambda a,b: a+b

result=f(5,6)
print(result)


'''
filter
map
reduce

'''
def is_even(n):
    return n%2==0


# filter

num=[2,55,33,4,66,98,78,100]
print(num)
even=list(filter(lambda n:n%2==0,num))
print(even)


#map
# if u want to change every value use map

square=list(map(lambda n:n*n,even))
print(square)

total=reduce(lambda a,b:a+b,square)
print(total)
