guests = []
name = input("Please enter the name of the person you want to invite (enter \"no\" to print list): ")
while name != "no":
    guests.append(name)
    name = input("Please enter the name of the person you want to invite (enter \"no\" to print list): ")
guests.sort()
for guest in guests:
    print(guest)