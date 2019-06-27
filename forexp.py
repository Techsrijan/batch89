'''range(10)
range(1,50)
range(1,10,2)
import time
for i in range(10):
    print(i,end="")

print("")
for j in range(1,10):
    print(j,end="")


print("")
for k in range(2,10,3):
    print(k,end="")


print("")
for m in range(20,10,-1):
    time.sleep(1)
    print(m)

lst=[1,55,88,33,44,333,34,33]
print(lst)

for k in lst:
    print(k)

for k in range(len(lst)):
    print(lst[k],",",end="")
print()
print("Table")
num=5
for p in range(1,11):
    t=num*p
    print("\n",t)'''

'''5*4*3*2*1=120
8*7*6*5*4*3*2*1=40320'''

for i in range(1,11):
    if i%3==0:
        #break
        #pass
        continue
    else:
        print(i)

else:print("nahi chalega")


i= 1
while i<=10:
    i = i + 1
    if i%4==0:
        continue
    else:
        print(i)


'''x= input("enter first number")
y= input ("enter second number")'''

x,y=input("enter two number").split()
x= int(x)
x=x+10
print(x,y)


x, y = [int(k) for k in input("Enter two value: ").split(",")]
x=x+10
print(x,y)

