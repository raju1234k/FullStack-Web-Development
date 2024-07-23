from  turtle import*
from random import randrange
from pygame import square , vector
import pygame
import time

food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)

dis_width = 900
dis_height = 600


def change(x,y):
    aim.x=x
    aim.y=y
def inside(head):
    return -200<head.x<190 and -200<head.y<190 

def move():
    head=snake[-1].copy()
    head.move(aim)
    
    if not inside ( head ) or head in snake:
      square(head.x,head.y,9,'red')
      update() 
      return


    snake.append()
    if head==food:
       print('snake',len(snake))
       food.x=randrange(-15,15)*10
       food.y=randrange(-15,15)*10

    else:
     snake.pop(0)

    clear()
 
    for body in snake:
       square(body.x,body.y,9,'green')

    square(food.x,food.y,9,'red')
    update()
    ontimer(move,100)   

    hideturtle()
    tracer(False)
    listen()
    onkey(lambda:change(10,0),'right')
    onkey(lambda:change(-10,0),'left')
    onkey(lambda:change(0,10),'up')
    onkey(lambda:change(0,-10),'down')

    move()
    done()

