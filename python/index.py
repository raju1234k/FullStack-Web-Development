import turtle
import colorsys

p=turtle.Turtle()
s=turtle.Screen()
s.title("studymuch")
s.bgcolor("black")
p.pensize(1.5)
p.speed(0)
n=36
h=0.5

for i in range(75):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    p.color(c)
    p.left(5)
    for j in range(5):
        p.forward(250)
        p.left(144)
turtle.done()        
