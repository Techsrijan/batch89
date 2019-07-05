import sys
n= sys.getrecursionlimit()
print(n)
sys.setrecursionlimit(2500)
print(sys.getrecursionlimit())

i=1

'''

when a function calls itself it is called recursion
'''
def greet():
    global i
    print(i,"Good Morning")
    i=i+1
    greet()

greet()
