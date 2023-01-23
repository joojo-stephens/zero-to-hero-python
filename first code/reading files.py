""" crops = open("inform.txt","r")
contents = crops.read()
print(contents)
 """
""" #reading individual line
crops = open("inform.txt","r")
first = crops.readline()
print(first)
second = crops.readline()
print(second) """

#reading from a csv file. the csv library can be of help
#first import csv
#using the "with" and "as" in the code
#using a loop
""" import csv
with open("inform.txt","r")as crops:
    rows = csv.reader(crops)
    for row in rows:
        print (row)
        for word in row:
            print(word) """

#removing the square brackets after displaying a list using a joint function
import csv
with open("inform.txt","r")as crops:
    rows = csv.reader(crops)
    for row in rows:
        print (",".join(row))
        