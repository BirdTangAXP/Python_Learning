import turtle
import math
import time


screen_size = 600
delay = 0.05
radius = 100




##set up screen
wn = turtle.Screen()
wn.title("Fourier Series Trial")
wn.bgcolor('white')
wn.setup(width = screen_size, height = screen_size)



line = turtle.Turtle()
line.speed(0)
line.shape("circle")
line.shapesize(0.1)


circle = turtle.Turtle()
circle.speed(0)
circle.shape("circle")
circle.color("blue")
circle.shapesize(0.1)




while True:
    
    wn.update
    circle.circle(radius,20)
    line.clear()
    line.penup()
    line.setposition(0,radius)
    line.pendown()
    line.goto(circle.xcor(),circle.ycor())
    

    

    time.sleep(delay)

wn.mainloop()


