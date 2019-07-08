from turtle import *

s=Turtle()
w=Screen()
#w.bgcolor('yellow')
w.title("My turtle")

s.shape('turtle')
lst=["red","yellow","orange","green","blue"]
s.penup()
s.goto(200,0)

for i in range(5):
    s.pendown()
    #s.begin_fill()
    #s.fillcolor(lst[i])
    s.pensize(10)
    s.pencolor(lst[i])
    s.circle(50)
    s.up()
    s.bk(100)

    #s.end_fill()


for i in range(150):
    s.color(lst[i%5])
    s.pensize(i/10+1)
    s.forward(i)
    s.left(60)

done()