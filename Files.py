from logging import FileHandler
#Declare a FileHandler to handle the opened file
FileHandler = open('test.txt', "r")
#read() is a function used in reading the file so it stores every of
#the file 
inp = FileHandler.read()
print(inp)

#We can ru through the file too using a for loop
#Example: For counting the number of lines in a file
count =  0 #we initialize a variable count for counting lines
for line in inp:
    count += 1
print(count)    