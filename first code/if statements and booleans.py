#using "if statemets"
favouriteteam = input("What is your favourite hockey team? ")
if favouriteteam == "Senators":
    print("Yeah Go Sens Go!")
    print("But I miss Alfie")
print("Great team of choice")

#converting input to match code
favouriteteam = input("What is your favourite hockey team? ")
favouriteteam = favouriteteam.capitalize()
if favouriteteam == "Senators":
    print("Yeah Go Sens Go!")
    print("But I miss Alfie")
print("Great team of choice")

#using comparisons
deposit = input("How much do you want to deposit?  ")
deposit = float(deposit)
if deposit > 100.0:
    print("You get a free toaster :)")
print("Have a nice day!")

#branching by using "else" and "else if"
deposit = input("How much do you want to deposit?  ")
deposit = float(deposit)
if deposit > 100.0:
    print("You get a free toaster :)")
else:
    print("Enjoy your sticker")
print("Have a nice day!")

#Boolean expressions
freetoaster = False 
deposit = input("How much do you want to deposit? ")
if float(deposit) > 100:
    freetoaster = True
if freetoaster:
    print("You get a free toaster!")