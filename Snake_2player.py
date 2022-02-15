import turtle
import time
import random


screen_size = 600
delay = 0.1
step = 20

#score

score = 0
score2 = 0
high_score = 0
speed = 0
global is_pause
is_pause = False


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
head.color("blue")
head.penup()
head.goto(-80,0)
head.direction = "stop"

# Snake2 head
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("green")
head2.penup()
head2.goto(80,0)
head2.direction = "stop"


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []
segments2 = []

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

    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y+step)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y-step)
    
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x-step)
    
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x+step)


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

def go_up2():
    if head2.direction != "down":
        head2.direction = "up"


def go_down2():
    if head2.direction != "up":
        head2.direction = "down"

def go_left2():
    if head2.direction != "right":
        head2.direction = "left"

def go_right2():
    if head2.direction != "left":
       head2.direction = "right"

def pause():
    global is_pause
    is_pause = not is_pause


def who_win(num):
    time.sleep(1)
    head.goto(-80,0)
    head.direction = "stop"

    head2.goto(80,0)
    head2.direction = "stop"

    global score
    global score2
    global speed
    score = 0
    score2 = 0
    speed = 0
    pen.clear()
    if num == "0":
        message ="  No one win!"
    else: 
        message = "  P"+num+" WON the game!"

    pen.write("P1 Score: {}  P2 Score : {} {} ".format(score, score2, message),align = "center", font=("Courier", 14,"normal"))


    for segment in segments:
        segment.goto(1000,1000)

    segments.clear()

    for segment in segments2:
        segment.goto(1000,1000)
    
    segments2.clear()


def check_border():
    border_h = wn.window_height()/2 - 10
    border_w = wn.window_width()/2 - 10
    if head.ycor() > border_h or head.ycor() < -border_h or head.xcor() > border_w or head.xcor() < -border_w:
        who_win("2")
    if head2.ycor() > border_h or head2.ycor() < -border_h or head2.xcor() > border_w or head2.xcor() < -border_w:
        who_win("1")

def check_bodycollision():
    for segment in segments:
        if segment.distance(head)< 20: 
            who_win("2")
        if segment.distance(head2)<20:
            who_win("1")

    
    for segment2 in segments2:
        if segment2.distance(head2)< 20: 
            who_win("1")
        if segment2.distance(head)<20:
            who_win("2")
    
    if head.distance(head2)<20:
        who_win("0")

   
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

wn.onkeypress(go_up2,"i")
wn.onkeypress(go_down2,"k")
wn.onkeypress(go_right2,"l")
wn.onkeypress(go_left2,"j")

wn.onkeypress(pause," ")

# Main game lop
while True:
    
    wn.update()
    
    if not is_pause:

     

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
            pen.write("P1 Score: {}  P2 Score : {}".format(score, score2),align = "center", font=("Courier", 14,"normal"))


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
        
        if head2.distance(food) < 20:
            # Move the food to a random place
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            food.goto(x,y)
            score2 += 10
            if speed < delay:
                speed += 0.005 
            if score > high_score:
                high_score = score
            
            pen.clear()
            pen.write("P1 Score: {}  P2 Score : {}".format(score, score2),align = "center", font=("Courier", 14,"normal"))


            #add a segment
            new_segments2 = turtle.Turtle()
            new_segments2.speed(0)
            new_segments2.shape("square")
            new_segments2.color("grey")
            new_segments2.penup()
            segments2.append(new_segments2)
        
        lenght2 = len(segments2)

        for i in range(lenght2-1,0,-1):
            x = segments2[i-1].xcor()
            y = segments2[i-1].ycor()
            segments2[i].goto(x,y)
            print("x:",x,"     y:",y)
            
        if lenght2 > 0:
            x = head2.xcor()
            y = head2.ycor()
            segments2[0].goto(x,y)
            print("go to head position")

        move()
        
        time.sleep(delay-speed)

wn.mainloop()

