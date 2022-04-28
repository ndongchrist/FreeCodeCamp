#A tuple is just like an unchangeagle list
tup = tuple()#Creating a tuple
tup = (12, 4, 79, 56)
print(max(tup))#max() returns the value in a tuple

#iterating through a tuple
for iter in tup:
    print(iter)#printing the each value in the tup

#Tuples are immutable
# #functions like Sort(), reverse(), append() don't function here in tuples.  

#using Dictionaries
person = dict()
person['name'] = 'Akashi'
person['age'] = 18
person['height'] = 3
tuple = person.items() #Actually Creates a list of tuples
#containing key,values pairs
print(tuple)