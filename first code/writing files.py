""" filename = "Guest.txt"
accessmode = "w"
myfile = open(filename, mode = accessmode) """

""" #writing into files
filename = "Guest.txt"
write = "w"
read = "r"
myfile = open(filename, mode = write)
 """
""" #if you don't want to overite texts typed in the .txt file the access mode should be append
filename = "Guest.txt"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = append) """

""" #writing to the file
filename = "Guest.txt"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = append)
myfile.write("Hi there! ")
myfile.write("How are you? ")

#sending it to a new line
filename = "Guest.txt"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = append)
myfile.write("\nHi there! ")
myfile.write("\nHow are you? ") """

""" #closing the file after finishing to write
filename = "Guest.txt"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = write)
myfile.write("Hi there! ")
myfile.write("\nHow are you? ")
myfile.close()
print("file written successfully") """

""" #creating a .csv file
filename = "Guest.csv"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = write)
myfile.write("susan, 29 ")
myfile.write("\nchris, 31 ")
myfile.close()
print("File written successfully") """

#asking for user info
data = input("please enter file info ")
filename = "data.txt"
write = "w"
read = "r"
append = "a"
myfile = open(filename, mode = write)
myfile.write(data)
myfile.close()
print("File written successfully")
