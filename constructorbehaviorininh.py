class A:
    def __init__(self):
        print("I am class A ")

class B(A):
    def __init__(self):
        super().__init__()
        print(" i am class B")


class C(B):
    def __init__(self):
        super().__init__()
        print("I am class C")


ob=C()
