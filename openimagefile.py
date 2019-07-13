f1=open("Koala.jpg","rb")

'''for data in f1:
    print(data)'''

f=open("Gola2.jpg","wb")

for data in f1:
    #print(data)
    f.write(data)

'''f.close()

f1.close()'''

'''f3 = open("Koala.jpg", "rb")
f4 = open("Gola.jpg", "wb")
for data in f3:
    print(data)
    f4.write(data)
    print("duplicate image created ")'''