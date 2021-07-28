#Simple Ping Pong game using Python
#Author: Abrar Islam
#Date; 07/28/2021

import turtle

screen = turtle.Screen()
screen.title("Ping Pong Game!")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle one:
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("green")
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle two:
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("green")
paddle_2.penup()
paddle_2.goto(350, 0)

# Ping Pong Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

# Score:
score1 = 0
score2 = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: 0   Player Right: 0", align="center", font=("Courier", 24, "normal"))
# Moving Function:
def paddle_1_up():
    y = paddle_1.ycor()
    y +=20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -=20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y +=20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -=20
    paddle_2.sety(y)
# Keyboard input:
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

# Main Game loop
while True:
    screen.update()

    #Move the ball:
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking:
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player Left: {}   Player Right: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player Left: {}   Player Right: {}".format(score1, score2), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and Ball collisions:
    if (ball.xcor() >340 and ball.xcor()< 350 )and (ball.ycor() < paddle_2.ycor()+40 and ball.ycor()> paddle_2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor()> -350 )and (ball.ycor() < paddle_1.ycor()+40 and ball.ycor()> paddle_1.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1



