s = {1,2,3,4,51,2,3}
print(s)
emptyset = {}
print(type(emptyset))

emptyset1=set()
print(type(emptyset1))

emptyset1 = set(s)
print(emptyset1)

set1 = {1,3,5,'ram',20.30}

print( 6 in set1)
print( 5 in set1)

print( 6 not in set1)
print( 5 not in set1)

set1.add(555)
print(set1)

set1.add(5)
print(set1)

s=  frozenset([1,2,4])
print(s)
#s.add(555)
#print(s)

set1.remove(555)
print(set1)


a= {1,2,3,4}
b= {2,4,3,7}

#union
print(a|b)
#intersection
print(a&b)

#diffrence
print(a-b) #which are in a but not in B
print(b-a) #which are in b but not in a

#symmertic difference
print(a^b) #not common in both a and b

print(len(a))

d=a.copy()
print(d)
print(d.clear())
#identity operator

x,y,z= 20,20,30
print("x=",id(x))
print("y=",id(y))
print("z=",id(z))

print( x is y)
print(x is z)
print(x is not y)
print(x is not z)

st = "abc"
st2= "abc"
print("st=",id(st))
print("st2=",id(st2))
print(st==st2)
print(st is st2)
print(st is not st2)


s1= input("enter your name")
print("S1=",s1)
print(id(s1))
s2= input("enter your name")
print("S2=",s2)
print(id(s2))

print(s1==s2)

print(s1 is s2)

'''
python creates two different objects that both store the same value
1. input of string from the console
2. input writing integer literals with manay digits
3. input writing floating point and complex litrels


'''
p=10.2
q=10.2
print (p is q)


l1=[1,1]
l2=[1,5]
print(l1<l2)