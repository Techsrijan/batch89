def passlist(ls):
    even_sum=0
    odd_sum=0
    for i in ls:
        if i % 2 == 0:
            print("even=", i)
            even_sum=even_sum+i
        else:
            print("odd=", i)
            odd_sum=odd_sum+i

    return even_sum,odd_sum


l=[2,88,7,77,55,56,24,]
x,y=passlist(l)
print("even sum",x)
print("odd sum",y)
print("even sum : {} and odd sum :{}".format(x,y))
