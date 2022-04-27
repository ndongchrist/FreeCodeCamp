
from logging import FileHandler


Filename = input('Type your File name: ')
try:
    FileHandler = open(Filename,'r')
except:
    print(f'File {Filename} cannot be opened')   
    quit() 
fhand1 = FileHandler.read()
count = 0
for line in fhand1:
    count =count + 1
print(f"The file {Filename} has {count} characters")    
