class A:
    def __init__(self):
        print("I am class A ")

class B():
    def __init__(self):
         print(" i am class B")

# MRO  : method resolution order   always runs the left class constructor
class C(B,A):
    def __init__(self):
        super().__init__()
        print("I am class C")


ob=C()