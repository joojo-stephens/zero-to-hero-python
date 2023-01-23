import csv
with open("Challenge 9.txt","r")as name:
    rows = csv.reader(name)
    for row in rows:
        print (",".join(row))