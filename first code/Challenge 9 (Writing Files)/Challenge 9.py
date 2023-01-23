filename = "Challenge 9.csv"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = write)
myfile.write("Doyle McCarty,27 ")
myfile.write("\nJody Mills, 25")
myfile.write("\nNicholas Rose, 32")
myfile.write("\nKian Goddard, 36")
myfile.write("\nZuha Hanania, 26")
myfile.close()
print("File written successfully")