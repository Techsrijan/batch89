from time import *
print(time())
print(localtime())
print(asctime())
print(asctime(localtime(time())))
print(clock())
lst = [3,4,5,6,7,8,7]
for i in lst:
    print(i)
    sleep(1)