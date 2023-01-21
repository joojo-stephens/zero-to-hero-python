import turtle
length = 0
angle = 0
pencolor = "red"
length = input("Specify yuor length? (input 0 to stop drawing) ")
length = int (length)
angle = input("Speciify your angle: ")
angle = int (angle)
pencolor = input("What pen color do your want to use? ")
     
while length != 0:
    turtle.color(pencolor)
    turtle.forward(length)
    turtle.right(angle)
    length = input("Specify yuor length? (input 0 to stop drawing) ")
    length = int (length)
    if length != 0:
        angle = input("Speciify your angle: ")
        angle = int (angle)
        pencolor = input("What pen color do your want to use? ")
print("nice")
