""" number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
result = number1 / number2
print(result)

#detect where error i likely to occur
#using "try" and "except" to handle error message
number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
try:
    result = number1 / number2
    print(result)
except:
    print("Oops! something went wrong!") """

#using the "sys.exc_info()" function to prompt the users of what went wrong
#first import sysnumber1 = float(input("input first number? "))
""" import sys
number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
try:
    result = number1 / number2
    print(result)
except:
    error = sys.exc_info()[0]
    print(error)
 """
#you specify how you will handle a particular error distinctively by knowing the name of the error
#you can know the name of the error by using the "sys.exc_info()[0]" display the type of error
import sys
number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
try:
    result = number1 / number2
    print(result)
#thw sys function displayed the ZeroDivisionError for us when i intentionally input error values
except ZeroDivisionError:
    print("The answer is underfined!")

#putting everything together
import sys
number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
try:
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("The answer is underfined!")
except:
    error = sys.exc_info()[0]
    print("Oops! something went wrong")
    print(error) 

#forcing the program to close when an error occurs by using the "sys.exit()"
import sys
number1 = float(input("input first number? "))
number2 = float(input("input second number? "))
try:
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("The answer is underfined!")
    sys.exit()
except:
    error = sys.exc_info()[0]
    print("Oops! something went wrong")
    print(error) 