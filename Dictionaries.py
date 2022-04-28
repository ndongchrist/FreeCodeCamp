from tabnanny import check


person = dict()
person['name'] = 'Akashi'
person['age'] = 18
person['height'] = 3
print(person)
#since five years passed since i was 18
person['age'] += 5
print(person)

#Dictionaries are used to perform a count of a number of 
#occurencies that occur in a list. For Example
Names = dict()#Creating a dictio...
list = ['Akashi', 'favour','jean', 'Delia','jean','favour','Akashi','jean']
for name in list:
    if name not in Names:#Checking if a key already exits in the Dictionary
        Names[name] = 1
    else:
        Names[name] += 1#increments the value of the key by 1
print(Names)       

#The get() method checks if a key:value already exits and if not it creats a 
#default pair
verify = Names.get('john', 4)
print(verify)
print(Names.keys())#Gives you all the keys
print(Names.values())#gives all the Values