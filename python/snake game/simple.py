import turtle
import random
import time

#creatimg screen layout
screen =turtle.Screen()
screen.title("snake game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("black")

#creating border line 

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score card 

score = 0
delay=0.1 

#snake 

snake= turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction='stop'

#food 

fruit= turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30,30)    

old_fruit=[]


#score card 
scoring= turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("score:",align="center",font=("courier",24,"bold"))

#define how to move 
def snake_go_up():
    if snake.direction !="down":
       snake.direction = "up"

def snake_go_down():
    if snake.direction !="up":
       snake.direction = "down"       

def snake_go_left():
    if snake.direction !="right":
       snake.direction = "left"

def snake_go_right():
    if snake.direction !="left":
       snake.direction = "right"      

def move():
    if snake.direction =="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction =="down":
        y=snake.ycor()
        snake.sety(y-20)    
    if snake.direction =="left":
        x=snake.xcor()
        snake.sety(x-20)
    if snake.direction =="right":
        x=snake.xcor()
        snake.sety(x+20)    

#keybord shortcutt
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")



