""" #first start with "def" and end with "return"
def printmessage():
    print("Hello World")
    return
printmessage()
 """
""" #using the "main()"" function to execute function below
def main():
    printmessage()
    return
def printmessage():
    print("Hello World")
    return
main() """

""" #using it for loops
def main():
    printnames()
    return
def printnames():
    names = ["Yess", "Hot", "Bread"]
    for name in names:
        print(name)
    return
main() """

#using parameters
def main():
    names = ["Yess", "Hot", "Bread"]
    lastname = input("Enter last guect? ")
    names.append(lastname)
    printnames(names)
    return
def printnames(booking):
    for name in booking:
        print(name)
    return
main()
