'''

type of method
1. instance method
2. class method
3. static method


'''

class student:
    school="techsrijan"
    #instance method
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def total(self):
        return (self.m1+self.m2+self.m3)


    @classmethod
    def displayschool(cls):
        print(cls.school)

    @staticmethod
    def msg():
        print("thank you for joining my school")


s=student(10,20,30)
print(s.total())

student.displayschool()

student.msg()