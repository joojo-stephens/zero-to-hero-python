name = input("What is your name?\n")
age = input("\nHow old are you?\n")
gender = input("\nWhat gender are you?\n")

name = name.capitalize()
age = age.lower()
gender = gender.lower()

print("\nI\'ve got a story for you :)")
print("Hello, my name is " + name + ". I\'m " + age + " years old. I am a lovely " + gender + ".")