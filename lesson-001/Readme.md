# Lesson 1: Say Hello

---
## helloworld.py
### Code
```python {.line-numbers}
print ("Hello World!")
```
### Run
~~~~shell {.line-numbers}
$ python3 helloworld.py
Hello World!
~~~~

---
## hello.py
### Code
~~~~python {.line-numbers}
name = input("What is your name? ")
print ("Hello %s!" % name)
offset = ''
for letter in name:
   offset += ' '
   print(offset+letter)
~~~~
### Run
~~~~shell {.line-numbers}
$ python3 hello.py 
What is your name? Tazkiyyah
Hello Tazkiyyah!
 T
  a
   z
    k
     i
      y
       y
        a
         h
~~~~

## Homework!
* Please read the [homework](Homework.md).
