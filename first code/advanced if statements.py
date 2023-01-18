""" #Using elif and else
isflyres = False
issenators = False
israngers = False
others = ("That\'s a nice team")
team = input("What is your favourite hockey team? ")
team = team.lower()
if team == "flyers":
    isflyres = True
elif team == "rangers":
    israngers = True
elif team == "senators":
    issenators = True

if isflyres:
    print("GO GO FLYERS!!")
elif israngers:
    print("LETS\'S GO RANGERS!")
elif issenators:
    print("GO! SENATORS GO!")
else:
    print(others) """

#using "and", "or"
#using "and"
""" isflyres = False
issenators = False
israngers = False
others = ("That\'s a nice team")
sports = input("What is your favourite sport? ")
team = input("What is your favourite hockey team? ")
team = team.lower()
if team == "flyers" and sports == "hockey":
    isflyres = True
elif team == "rangers" and sports == "hockey":
    israngers = True
elif team == "senators" and sports == "hockey":
    issenators = True

if isflyres:
    print("GO GO FLYERS!!")
elif israngers:
    print("LETS\'S GO RANGERS!")
elif issenators:
    print("GO! SENATORS GO!")
else:
    print(others) """

""" #using "or"
tns = False
sport = input("What is your favourite sport? ")
team = input("What is your favourite team? ")
sport = sport.lower()
team = team.lower()
if team == "tottenham" or sport == "soccer":
    tns = True 

if tns:
    print("Here is your crown, KING!")
else:
    print("nice taste!") """

""" #combining "and", "or"
country = input("What's the name of your country? ")
pet = input("What's the name of your pet? ")
country = country.lower()
pet = pet.lower()
if country == "canada" and (pet =="moose" or pet == "beaver"):
    print("Do you play hockey too?" )
print("Nice!") """

""" sport = input("What is your favourite sport? ")
team = input("What is your favourite team? ")
sport = sport.upper()
team = team.upper()
sportIsHockey = False
if sport == 'HOCKEY':
    sportIsHockey = True
teamIsCorrect = False
if team == 'SENATORS' or team == 'LEAFS':
    teamIsCorrect = True
if sportIsHockey and teamIsCorrect:
     print('Good luck getting to the cup this year')
print("Yeah") """

# nesting if statements
freshcoffee = True
monday = False
day = input("What day is it? ")
coffee = input("Have you had a fresh coffee? ")
day = day.lower()
coffee = coffee.lower()
if day == "monday":
    monday = True
if coffee == "no":
    freshcoffee = False

if monday:
    if not freshcoffee:
        print("go buy a coffee!")
    print("I hate mondays")
print("You can start work")
