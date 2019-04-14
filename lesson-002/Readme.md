# Lesson 2: Types & Fun

## Introduction

There are all types of objects or things around us. There are fish, kites, cars, pens,
spoons, knives, ships, markers & more.

Each type of object has different properties, for example for a car, we can talk about:
* It's manufacturer: Nissan, Mercedes, Toyota or others.
* The year it was made
* The color of the car
* Is it new or used
* What kind of car is it? Compact, Sedan, SUV or something else?

Each type of object can perform different actions, consider a car and a pen.
* A car can drive. A pen cannot drive.
* A pen can write, A car cannot drive.
* A car can slow down or speed up. A pen cannot.

When we talk about an object, we talk about it's type. Based on the type of the object, we
can then talk about it's properties and it's actions, or what it can do. 

In computer languages we use different object types. When we talk about their _properties_, we
refer to these as these as _attributes_. When we talk about their actions, we refer to these
as their _methods_.

For example when we use an integer object we talk about it's attributes such as it's value and 
it's methods such as sqaure root. 

Depending on the type of the object used in Python, it will have different attributes & methods.

## Integer Types
~~~~python
>>> x=8
>>> type(x)
<class 'int'>
>>> x/2
4.0
~~~~
* In the example above _x_ is a variable of type integer (int). Python infers the type based on the value assigned, in this case 4 which is an integer.
* We can do division on _x_ since it's an integer.
* If we try to do an operation on _x_ that would not work on an integer we get an error.
~~~~python
>>> x.upper()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x.upper()
AttributeError: 'int' object has no attribute 'upper'
~~~~
* We tried to do a case conversion on an integer, this is not allowed on an integer.

## String Types
* Consider now if we had assigned _x_ a string (str) value
~~~~python
>>> x='a'
>>> type(x)
<class 'str'>
>>> x.upper()
'A'
~~~~
* The same code works, _x.upper()_ is allowed since the type of _x_ is a string and strings can be converted to uppercase.

## Is _1_ the same as _"1"_?
* Take a look at the [add.py](add.py) code example
~~~~python
x = input("enter x: ")
y = input("enter y: ")
z = int(x) + int(y)
s = str(x) + str(y)
print(x, "+", y, "is: ", z)
print(x, "+", y, "is: ", s)
~~~~
* When we run this code, the effect we get depends on how we handle the type.
* If we use the _str(x)_ instead of _int(x)_ type the effect of adding the variables has a diferent result.
* Integer addition sums the values.
* String addition appends the two values to produce a single result.
~~~~python
enter x: 1
enter y: 2
1 + 2 is:  3
1 + 2 is:  12
~~~~
* Go ahead and have some fun playing around in IDLE with types.


## Homework!
* Please read the [homework](Homework.md).
