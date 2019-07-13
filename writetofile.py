f1=open("ram.txt","r")
f=open("shyam1.txt","w")

for data in f1:
    #print(data)
    f.write(data)

f.close()

f=open("shyam1.txt","r")
for data in f:
    print(data)