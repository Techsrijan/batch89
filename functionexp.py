def person(name,age):
    print("name=",name)
    age=age+10
    print("age=",age)


#1. postional arguments
person("ashwani",35)

# person(22,"abcd")  problem arises

'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument 

'''

person(name="ashwani kumar",age=236)
person(age=100,name="ABCD")

def persondata(name,lastname,age=18):
    print("name=", name)
    print("lastname=", lastname)
    print("age=", age)

persondata("ashwani","kumar")
persondata("ashwani","kumar",33)

persondata(age=22,name="ashwani",lastname="kumar")

def add(x,y,z):  #here x,y are called formal argument
    res=x+y+z
    print("result=",res)

add(5,2,6)

#variable length argument
#def subzod(a,*b):
def subzod(*b):
    c=0
    # print(a)
    #print(b)
    for i in range(len(b)):
        c=c+b[i]
    print(c)

subzod(1,2,3,4,5,6,54,5445,454545,45454)