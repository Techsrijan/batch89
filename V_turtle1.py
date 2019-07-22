"""from turtle import *
s = Turtle()  #s is the object of Turtle class
w = Screen() #w is  the object of Screen claa
s.shape("turtle")
s.speed(1)
w.title("Vish Turtle")
#s.write("Vishal")
#w.bgcolor("yellow")
s.color("green")

s.pencolor("Blue")
s.pensize(5)

s.begin_fill()
for i in range(4):

    s.forward(100)
    s.left(90)

s.end_fill()
s.up()
s.backward(150)
s.down()
s.color("orange")
s.pencolor('blue')
s.begin_fill()
for j in range(4):

    s.forward(100)
    s.left(90)

s.end_fill()
s.up()
s.goto(-100,90)
s.down()
s.begin_fill()
s.stamp()
s.shape('circle')

s.circle(100,steps=10)


s.end_fill()
done()"""

import turtle

ninja = turtle.Turtle()

ninja.speed(100)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()