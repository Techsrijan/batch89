#sum of Natural Numbers using Recursion
def sumofnn(num):
    s=0
    if num == 1:
        return num
    s = num + sumofnn(num-1)
    return s

print(sumofnn(5))