from turtle import *

s=Turtle()
w=Screen()
#w.bgcolor('yellow')
w.title("My turtle")

s.shape('turtle')
s.pensize(10)
lst=["red","yellow","orange","green","blue"]
for i in range(5):
    s.pencolor(lst[i])
    s.forward(200)
    s.left(144)
    #s.bk(100)

done()