import turtle
length = 0
angle = 0
while length != 0:
    length = input("Specify yuor length? ")
    angle = input("Speciify your angle: ")
    turtle.forward(length)
    turtle.right(angle)
print("nice")