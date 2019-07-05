def recf(n):
    if n==0:
        return 1
    else:
        return n*recf(n-1)


def add(x,y):  #here x,y are called formal argument
    res=x+y
    print("result=",res)


def sub(x,y):  #here x,y are called formal argument
    res=x-y
    print("result=",res)




'''
add(5,5)
sub(9,5)
print(recf(5))'''

print("Calc=",__name__)

if __name__== "__main__":
    def developer():
        print("Techsrijan")


developer()
