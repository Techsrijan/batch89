from turtle import *
s= Turtle()
s.pensize(10)
lst=["red","black","blue","green","orange"]
s.begin_fill()
s.color("pink")

for i in lst:
    s.pencolor(i)
    s.forward(250)
    s.left(144)
s.end_fill()
done()