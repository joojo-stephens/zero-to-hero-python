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