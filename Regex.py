
import re #importing the regular exp library
#creating a text to check the numbers init.
text = "My 2 favourite Numbers are 30 and 1"
#the findall() uses the re in the brackets to scan the text 
#and find the pattern that matches and stores it in a list.
find = re.findall("[0-9][0-9]?",text)
print(find)
