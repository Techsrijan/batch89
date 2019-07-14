''''
variable
  1. instance varable
  2. class varable(static variable)

namespace--- is an area where you can create and store object/variable
1. class namespace
2. object/instance namespace
'''



class Car:
    wheel=4 #class varable(static variable)
    def __init__(self):
        self.mil=10 #instance varable
        self.speed=100



maruti=Car()
print("mil=",maruti.mil,"speed=",maruti.speed,"wheel=",maruti.wheel)
maruti.mil=25
print("mil=",maruti.mil,"speed=",maruti.speed,Car.wheel)