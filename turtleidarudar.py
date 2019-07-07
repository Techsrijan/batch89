from turtle import *

def sq():
    s.begin_fill()
    for i in range(4):
        s.forward(100)
        s.left(90)

    s.end_fill()


s=Turtle()
w=Screen()
#w.bgcolor('yellow')
w.title("My turtle")

s.shape('turtle')


s.color('#A92707')
s.speed(1)
s.pencolor('red')
s.pensize(5)

'''s.left(40)
s.forward(100)'''
s.up()
s.goto(100,-90)
s.down()
sq()


s.forward(200)
#s.reset()
#s.undo()
sq()

done()