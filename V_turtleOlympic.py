from turtle import *
s=Turtle()
w=Screen()
#w.bgcolor('yellow')
w.title("Olympic turtle")
s.speed(10)
s.shape('turtle')
lst=["red","black","blue"]
lsst=["green","orange"]

s.penup()

s.goto(100,0)
for i in lst:
    s.pendown()
    #s.begin_fill()
    #s.fillcolor(lst[i])
    s.pensize(8)
    s.pencolor(i)
    s.circle(50)
    s.up()
    s.bk(120)


s.goto(40,-50)
for i in lsst:
    s.pendown()
    #s.begin_fill()
    #s.fillcolor(lst[i])
    s.pensize(8)
    s.pencolor(i)
    s.circle(50)
    s.up()
    s.bk(120)
    #s.end_fill()
done()