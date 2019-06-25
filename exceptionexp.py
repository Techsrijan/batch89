lst = [1,2,3,5]

try:
    print("freez is open")
    a=int(input("enter first number"))
    b=int (input("enter second number"))
    d = a/b
    print(d)
    print("divide ho gaya")
    print(lst[20])
    # print("freez is close")

except ZeroDivisionError as e:
    print("B can not be zero",e)
    #print("freez is close")

except IndexError as e:
    print("you are accress the out of range element",e)
    #print("freez is close")


except Exception as e:
    print("pagla gaye ho ka",e)
    #print("freez is close")

finally:
    # it always executes
    print("freez is close")

#lst[5]
print("thank you")
print("freez is close")