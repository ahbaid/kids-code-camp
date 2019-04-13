import turtle
colors=['pink','blue','orange','purple','yellow']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
   t.pencolor(colors[x%5])
   t.width(x/100+1)
   t.forward(x)
   t.left(73)
