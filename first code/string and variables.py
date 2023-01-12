# using the "input" command to get information from the users
name = input("What is your name? ")
print(name)

# using the same variable for a different value
name = input("What is your name? ")
print(name)
name = "Mary"
print(name)

# Concatenating strings
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
print("Hello " + firstname + " " + lastname + ".")

# some pretty neat functions you can use to manipulate strings
message = "Hello World"
print(message.lower())
print(message.upper())
print(message.swapcase())

name = input("What is your name? ")
country = input("What country do you live in? ")
country = country.upper()
print("\nHello " + name + ".\nYou live in " + country +"!.")

# other neat functions
message = "Hello world"
print(message.find("world"))
print(message.count("o"))
print(message.capitalize())
print(message.replace("Hello","Hi"))

# Giving python a hint
postalcode = " "
# this informs python that we are ddealing with a string here
postalcode = input("What is your postal address? ")
print(postalcode.upper())