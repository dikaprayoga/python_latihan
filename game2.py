import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title('game by dkkz2')
wn.bgcolor('red')
wn.setup(width=600, height=600)
wn.tracer(0)
    
    
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0,0)
head.direction() = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

while True:
    wn.update()

    move()

wn.mainloop()
