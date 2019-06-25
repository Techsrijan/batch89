
av= 10
n= int(input("how many candy u want"))
print(n)


i=1
while i<=n:
    if av >= i:
        print(i,"=","Collect Candy")
    else:
        print("Out of stock")
        break
    i=i+1

else: # this else will run when the loop properly works
    print("thank you Please visit again")