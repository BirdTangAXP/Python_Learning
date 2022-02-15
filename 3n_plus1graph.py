import turtle


n = 100
bird_num = []
bird = []
bird_num.append(0)
bird_num.append(1)
mile = 20
angle = 15
line = 1
c_change = 5
turn = 0

bird.append(turtle.Turtle())
bird.append(turtle.Turtle())
bird[0].shape("circle")
bird[0].shapesize(0.05)
bird[0].speed(0)
bird[1].shape("circle")
bird[1].shapesize(0.05)
bird[1].speed(0)
bird[1].screen.colormode(255)
bird[1].color((255,1,1))



while line < 255:
    for i in range(1,line+1):
        turn =turn +1
        bird_num[i] = bird_num[i]*2
        bird[i].right(angle)
        bird[i].forward(mile)
        if line < 255:
            bird[i].color((255-line,line,line))
        upper = (bird_num[i]/2)-1
        if upper/3 > 1 and upper%3 == 0 and upper/3%2!=0:
            bird_num.append(upper/3)
            bird.append(bird[i].clone())
            if line < 255:
                bird[line].color((255-line,line,line))
            bird[line].left(angle)
            bird[line].forward(mile)
            print("turn: ", turn,"line: ",line,"last Number:", bird_num[i]/2,"Number:",bird_num[line+1])
            line = line+1
            





turtle.done()