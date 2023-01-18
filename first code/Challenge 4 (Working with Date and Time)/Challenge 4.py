
import datetime
userinput = input("Please input the time for the deadline? (dd-mm-yyyy) ")
deadlinedate = datetime.datetime.strptime(userinput,"%d-%m-%Y").date()
currentdate = datetime.date.today()
difference = deadlinedate - currentdate
print(difference.days)
print ("The number of days left until deadline is {0:.0f} days".format(difference.days))
weeks = difference.days/7
print ("The number of weeks left until deadline is {0:.0f} weeks".format(weeks))
months = difference.days/30
print ("The number of months left until deadline is {0:.0f} months".format(months))
years = difference.days/365
print ("The number of years left until deadline is {0:.0f} years".format(years))