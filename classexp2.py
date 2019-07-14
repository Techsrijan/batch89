class Student:
    def print_info(self):
        print("student name is abc")

    def student_data(self,name,roll):
        self.name=name
        self.roll=roll
        print("Name=",self.name,"rollno=",self.roll)
    # constructor which runs automatically when the object is created
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        print("Name=", self.name, "rollno=", self.roll)
        print("run kab karega dekhna hi")

s=Student("Ram",56)
s.print_info()
s.student_data('ashwani',22)
'''s2=Student()
s2.student_data('Mohan',55)'''
s3=Student("delhi",55)
#Student.print_info(s)