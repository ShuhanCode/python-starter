import turtle


sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width = 1000, height = 600)



left_pad=(turtle.Turtle())
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)



right_pad=(turtle.Turtle())
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("blue")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5


left_player = 0
right_player = 0




sketch = turtle.Turtle()
sketch.speed(0)
sketch.color('black')
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write('Left player:0, Right player:0', align='center', font=('Courier',24,'normal'))




def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def paddlebup():
    y =  right_pad.ycor()
    y+= 20
    right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)



sc.listen()
sc.onkeypress(paddleaup, 'w')
sc.onkeypress(paddleadown, 's')
sc.onkeypress(paddlebup, 'Up')
sc.onkeypress(paddlebdown, 'Down')



while True:
    sc.update()
 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
 
    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
 
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
 
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
 
    # Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+40 and ball.ycor() > right_pad.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
        
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_pad.ycor()+40 and ball.ycor()>left_pad.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1
