a = 5
print(type(a))

'''
object is an entity which can be uniquely identified in the real world.
car,fruit - class
class - group of similar object.
each of has two characteristics--
1. state
2. behavior
maruti 800 up53 a 120--object
state
    color
    weight
    model no
    height
bechaivor:
    ingnition system()
    apply break()
    apply accelerator()


class
   object

class
    state
    behavior

class
     variable
     function/method


class -- is blueprint that represents state and behavior of the 
         object of same kind.  

object == is an instance of a class.                           
'''
"""
#simple class object created
class Info:
    name = "My name is Vishal"

obj = Info()
print(obj.name)
"""

"""class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Hello Ji")

p1= Person("Vishal",22)
print(p1.name)
print(p1.age)"""


#Addition program with class object
class Addition:
    first = 0
    second = 0
    add = 0

    def __init__(self,f,s):     #parameterized constructor
        self.first = f
        self.second = s

    def calculate(self):
        self.add = self.first + self.second

    def display(self):
        print("First No. :",self.first)
        print("Second No. :",self.second)
        print("Sum is :",self.add)

a = Addition(5,6)
a.display()
a.calculate()
