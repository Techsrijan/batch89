from time import *
#return no of second from 1970 to today
#https://www.guru99.com/date-time-and-datetime-classes-in-python.html
print(time())
print(localtime())
print(asctime())
print(asctime(localtime(time())))
print(clock())
lst = [3,4,5,6,7,8,7]

for i in lst:
    print(i)
    sleep(1)

