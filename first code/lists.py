guests = ["Christopher", "Susan", "Bill", "Satya"]
print(guests[0])

#printing counting backwards of the list
guests = ["Christopher", "Susan", "Bill", "Satya"]
print(guests[-1])

#Changing the value of a list
guests = ["Christopher", "Susan", "Bill", "Satya"]
print("First value is " + guests[0])
guests[0] = "Steve"
print("First value is now " + guests[0])

#Values are added to the list using the "append()" function
guests = ["Christopher", "Susan", "Bill", "Satya"]
guests.append("Steve")
print(guests[-1])

#Values can be removed from the list using the "remove()" function
guests = ["Christopher", "Susan", "Bill", "Satya"]
guests.remove("Christopher")
print(guests[0])

#use the "del" function to delet entries in the list if you don't want to use their names
guests = ["Christopher", "Susan", "Bill", "Satya"]
del guests[0]
print(guests[0])

#Searching for the position of a value using the "index()" function
guests = ["Christopher", "Susan", "Bill", "Satya"]
print(guests.index("Bill"))

#Using a loop
guests = ["Christopher", "Susan", "Bill", "Satya"]
for steps in range(4):
    print (guests[steps])

#using the "len()" function to determine how many values are in the list
guests = ["Christopher", "Susan", "Bill", "Satya"]
entries = len(guests)
for steps in range(entries):
    print (guests[steps])

#You can just tell the loop to go through your list
guests = ["Hot","Christopher", "Susan", "Bill", "Satya"]
for guest in guests:
    print(guest)

#Sorting lists in alphabetical order using the "sort()" function
guests = ["Hot","Christopher", "Susan", "Bill", "Satya"]
guests.sort()
for guest in guests:
    print(guest)