from logging import FileHandler
#Declare a FileHandler to handle the opened file
FileHandler = open('test.txt', "r")
#read() is a function used in reading the file so it stores every of
#the file 
inp = FileHandler.read()
print(inp)