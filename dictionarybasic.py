temp={}
print(type(temp))
temp['mohan']=25
temp['sohan']=36
temp['rohan']=40
print(temp)

mobile ={'Ram':'lg','shyam':'mi'}

print(mobile)

print(temp.keys())
print(temp.values())


s=dict()
print(s)
s=dict(temp)
print(s)

#delete
print("ok")
del temp['sohan']
print(temp)

print(len(s))

