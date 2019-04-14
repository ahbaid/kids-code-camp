# neatsquare.py
import turtle
colors=['red','blue','green','yellow','white','orange']
t=turtle.Pen()
turtle.bgcolor('black')
t.width(10)
for x in range(1000):
   t.pencolor(colors[x%5])
   t.forward(200)
   t.left(90)
