#working with dates 
#first you need to import datetime
import datetime
currentdate = datetime.date.today()
print(currentdate)
#displaying different parts of the date
print(currentdate.year)
print(currentdate.month)
print(currentdate.day)
#using "strftime" to change the format in which date is displayed
print(currentdate.strftime("%d %b, %Y"))

#using dates in a sentence
import datetime
currentdate = datetime.date.today()
print(currentdate.strftime ("Please attend our event %A, %B %d in the year %Y"))

#converting  string to a date
import datetime
currentdate = datetime.date.today()
userinput = input("Please enter your birthday? ")
birthday = datetime.datetime.strptime(userinput,"%d-%m-%Y").date()
print(birthday)

#telling the user to enter their input in a specific order
import datetime
currentdate = datetime.date.today()
userinput = input("Please enter your birthday? (dd-mm-yyyy) ")
birthday = datetime.datetime.strptime(userinput,"%d-%m-%Y").date()
print(birthday) 

 #creating a countdown until someones birthday
import datetime
userinput = input("Please input your birthday? (dd-mm-yyyy) ")
yourbirthday = datetime.datetime.strptime(userinput,"%d-%m-%Y").date()
currentdate = datetime.date.today()
nextbirthday = yourbirthday - currentdate
print (nextbirthday.days)

#working with times
import datetime
currenttime = datetime.datetime.now()
print (currenttime)
print (currenttime.hour)
print (currenttime.minute)
print (currenttime.second)

#using "strftime" format
import datetime
currenttime = datetime.datetime.now()
print(datetime.datetime.strftime(currenttime,"%H:%M:%S"))
