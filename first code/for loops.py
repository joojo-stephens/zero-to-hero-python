""" import turtle
#use "turtle.Screen().exitonclick()" to maintain the window after running turtle
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.forward(100)
turtle.Screen().exitonclick()

#you can use colors in turtle
import turtle
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.forward(100)
turtle.Screen().exitonclick()

#using loops for repeated commands
import turtle
for steps in range(3):
    turtle.forward(100)
    turtle.right(90)
turtle.Screen().exitonclick()


#only indented code is repeated
import turtle
for steps in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.color("red")
turtle.forward(200)
turtle.Screen().exitonclick() 

#using nested loops
import turtle
for steps in range(5):
    turtle.forward(100)
    turtle.right(360/5)
    for moresteps in range(5):
        turtle.forward(50)
        turtle.right(360/5)
turtle.Screen().exitonclick()

#using a variable to represent number of sides
import turtle
sides = input("How many sides do you want? ")
sides = int(sides)
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
turtle.Screen().exitonclick()

#using loops to skip values
import turtle
sides = 10
for steps in range(1,sides,2):
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
turtle.Screen().exitonclick()

#telling the values exactly what you want
import turtle
sides = 6
for steps in [1,2,3,4,5]:
    turtle.forward(100)
    turtle.right(360/sides)
    for moresteps in range(sides):
        turtle.forward(50)
        turtle.right(360/sides)
turtle.Screen().exitonclick()

import turtle
for steps in ["blue","red","green","black"]:
    turtle.color(steps)
    turtle.forward(100)
    turtle.left(90)
turtle.Screen().exitonclick() """