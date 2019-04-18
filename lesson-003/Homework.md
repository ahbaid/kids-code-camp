# Homework - Lesson 003

## Introduction
You've learned so much, it's time for some fun.
Have you ever played with an etch-a-sketch? Well it's time to do so!

Python has many packages that you can use to get additional functionality.

What's a package you ask? Think of it like a book you can borrow and use.

Depending on what you are doing you would get the appropriate book. For 
example if you are cooking you'd get a cookbook. If you are learning to 
draw you may get a book on art.

We will be working with some graphics, so we will be using a package that
helps us to play around.

Don't worry too much about what packages are, we'll get into that later.

For now, let's have some fun! Follow along.

## Turtle graphics
* Python provides a package known as "turtle".
* We will import this and play along.
* Just type in the following code and see what happens.
* Open up IDLE and begin.

## Turtle Code
* First, we'll get the turtle package loaded
~~~~python
import turtle
~~~~

* Now let's create a turtle
~~~~python
t=turtle.Pen()
turtle.bgcolor('black')
t.color('red','yellow')
~~~~

* Now you should see an arrow head on a black canvas.
* It doesn't look like a turtle at all.
* The turtle has a pen it drags along. Let's set the color and width of that pen.
~~~~python
t.pencolor('yellow')
t.width(5)
~~~~

* Now let's move, notice how the pen leaves a line behind the turtle.
~~~~python
t.forward(100)
~~~~

* Now turn left (90 degrees) change colors and draw another line
~~~~python
t.left(90)
t.pencolor('red')
t.forward(100)
~~~~

## Homework
### For those up to 10:
1. Draw a rectangle
2. Draw a square

### For those up to 12:
3. Draw an equilateral triangle 
4. Draw a scalene triangle

### For those up to 14:
5. Draw a pentagon
6. Draw a hexagon

### For those 16 and older:
7. Do a dir(turtle), examine the methods you can use. Is there a way to lift the turtle's pen?
8. If there is a way to lift and lower the turtle's pen, draw two squares next to each other.
