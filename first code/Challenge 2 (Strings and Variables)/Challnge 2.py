name = input("What is your name?\n")
age = input("\nHow old are you?\n")
gender = input("\nWhat gender are you?\n")

name = name.capitalize()
age = age.lower()
gender = gender.lower()

print("\nI\'ve got a story for you :)")
print("Hello, your name is " + name + ". You\'re " + age + " years old. You are lovely " + gender + ".")