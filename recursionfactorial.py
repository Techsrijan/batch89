def recf(n):
    if n==0:
        return 1
    else:
        return n*recf(n-1)

res= recf(15)
print(res)