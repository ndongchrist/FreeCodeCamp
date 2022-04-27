
#Declare a FileHandler to handle the opened file
FileH = open('test.txt')
lines = FileH.read()

#We can read through the file too using a for loop
#Example: For counting the number of lines in a file
count =  0 #we initialize a variable count for counting lines
for line in lines:
    count += 1
print(count)    

#Searching Through a file
for line in FileH:
    line = line.rstrip()
    if not 'hello' in line:
        continue
    print(line)
