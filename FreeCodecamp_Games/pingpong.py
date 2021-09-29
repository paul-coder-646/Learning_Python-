# TODO 
# 1) make this object oriented
# 2) add randomness to initial ball speed 
# 3) maybe add levels

import turtle, random

# Setup Gui / Playground
window = turtle.Screen()
window.title('Pong by Paul')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_left = 0
score_right = 0

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup() # as we don't wanna leave prints where the paddle moved, we just suspend the pen :)
paddle_left.goto(-350, 0)


# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.penup() # as we don't wanna leave prints where the paddle moved, we just suspend the pen :)
paddle_right.goto(350 , 0)

# Ball
# for the ball we don't need .shapesize() as the default parameters work just fine :D
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup() # as we don't wanna leave prints where the paddle moved, we just suspend the pen :)
ball.goto(0 , 0) # spawn in the center
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player Left: 0 Player Right: 0", align="center", font=("Courier", 24, "normal"))

#Border (The line deviding the playing field)
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.hideturtle()
border.goto(0, 240)
border.right(90)
# dot the line downward towards the bottom :)
for i in range(25):
    border.dot()
    border.forward(20)
    

# Movement

# function move the left paddle up
def paddle_left_up():
    y = paddle_left.ycor()
    if y > 220:
        return
    y += 30
    paddle_left.sety(y)

# function to move the left paddle up
def paddle_left_down():
    y = paddle_left.ycor()
    if y <= -220:
        return
    y -= 30
    paddle_left.sety(y)

# function to move the left paddle up
def paddle_right_up():
    y = paddle_right.ycor()
    if y > 220:
        return
    y += 30
    paddle_right.sety(y)

# function to move the left paddle up
def paddle_right_down():
    y = paddle_right.ycor()
    if y <= -220:
        return
    y -= 30
    paddle_right.sety(y)

# Keyboard binding for movement
window.listen()
window.onkeypress(paddle_left_up, 'w')
window.onkeypress(paddle_left_down, 's')
window.onkeypress(paddle_right_up, 'Up')
window.onkeypress(paddle_right_down, 'Down')



# Main game loop
def play():

    global score_left
    global score_right

    while True:
        #update the game so everything gets (re)evaluated
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        # Top 
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        
        # Bottom
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Right
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_left += 1
            pen.clear()
            pen.write("Player Left: {} Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))
        
        # Left
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_right += 1
            pen.clear()
            pen.write("Player Left: {} Player Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

        # Collision detection right side
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 50 and ball.ycor() > paddle_right.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            

        # Collision detection left side
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 50 and ball.ycor() > paddle_left.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

if __name__ == '__main__':
    play()
