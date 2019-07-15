'''
Deriving a new class from the base class is known as inheritance
types of inheritance:
1. single level inheritance
2. multilevel inheritance
3. hierarchical inheritance
4.multiple inheritance
5.hybrid inheritance

'''


#room is base class or parent class
class Room:
    def get_roominfo(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return(self.l*self.b)

#guestroom is derived class or child class
class GuestRoom(Room):
    def info(self):
        print("Beautiful Room")




'''r=Room()
r.get_roominfo(20,60)
print("area of room=",r.area())'''

x=GuestRoom()
x.info()
x.get_roominfo(50,40)
print("area of room=",x.area())