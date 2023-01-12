# calculating the are of a triangle
# i am telling python that we are going to be working with numbers
area = 0
height = 10
width = 20
area = 1/2*(height*width)
print(area)
# formating the numbers to display them with string
# "%f" was used because the value of are is a float number
print ("the area of the triangle is %0.2f" %area)

# using the "%d" format
print("my fav number is %06d" %42)

# using the ".format()" method
print("the area of the trangle will be {0:f}" .format(area))

#using the ".format()" method for multiple numbers
print("Here are three numbers. The first one is {0:.0f} " \
    "the second one is {1:.2f} and the third one is {2:.6f}" .format(7,8,9))

#Collecting inpust frum users
salary = input("What is your salary? ")
bonus = input("What is your bonus? ")
total = float(salary) + float(bonus)
print("Your total amount of money is GHc {0:.0f}" .format(total))