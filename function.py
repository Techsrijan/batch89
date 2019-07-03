from math import sqrt
'''
void sum(int x,int y)
{
int c= x+y;
printf("%d",c);
}
sum(50,20);



int sum(int x,int y)
{
int c= x+y;
return c;
}
a=sum(2,5)
printF("%d",a)


'''
#print("Good Morning")

#function definition

#user defined funtion
def greet():
    print("Good Morning")

#function call
greet()
greet()
greet()


def add(x,y):  #here x,y are called formal argument
    res=x+y
    print("result=",res)
    greet()

a=int(input("enter Any number"))
b=int (input("enter Any number"))

add(a,b)  #here a,b are called actual argument
add(5,10)
greet()
add(400,500)


def sub(p,q):
    m=p-q
    return m

d = sub(100,6)
print(d)

# Library function
x= sqrt(36)
print(x)

def calc(c,d):
    mul=c*d
    div= c/d
    #print(mul,div)
    return mul,div

x,y=calc(55,11)

print("mul=",x,"\n div=",y)
