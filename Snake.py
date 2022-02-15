import turtle
import time
import random


screen_size = 600
delay = 0.1
step = 20

#score

score = 0
high_score = 0
speed = 0


##set up screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width = screen_size, height = screen_size)
wn.tracer(0)  # turn of the screen update

# Snake1 head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"



# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+step)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-step)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-step)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+step)


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
       head.direction = "right"

def game_over():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    global score
    global speed
    score = 0
    speed = 0
    pen.clear()
    pen.write("Score: {}  Hight Score : {}".format(score, high_score),align = "center", font=("Courier", 14,"normal"))


    for segment in segments:
        segment.goto(1000,1000)

    segments.clear()

def check_border():
    border = screen_size/2 - 10
    if head.xcor() > border or head.xcor() < -border or head.ycor() > border or head.ycor() < -border:
        game_over()

def check_bodycollision():
    for segment in segments:
        if segment.distance(head)< 20:
            game_over()
   
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score = 0", align="center",font=("Courier", 14,"normal"))


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

# Main game lop
while True:


    wn.update()

    check_border()
    check_bodycollision()

    if head.distance(food) < 20:
        # Move the food to a random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        score += 10
        if speed < delay:
            speed += 0.005 
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score : {}".format(score, high_score),align = "center", font=("Courier", 14,"normal"))


        #add a segment
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("grey")
        new_segments.penup() 
        segments.append(new_segments)
    
    lenght = len(segments)

    for i in range(lenght-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
        print("x:",x,"     y:",y)
        
    if lenght > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        print("go to head position")
        

        print(lenght)

    move()
    
    time.sleep(delay-speed)

wn.mainloop()

