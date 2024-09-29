# A dictionary in Python is a collection of key-value pairs. Each key is connected 
# to a value, and you can use a key to access the value associated with that key.

alien_0 = {'color': 'green', 'points': 5}

#Accessing value from dictionary
print(alien_0['color'])

#Dictionaries are dynamic structures,you can add new key-value pairs to a dictionary at any time 

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['x_incr'] =0
alien_0['y_incr'] =20
alien_0['speed']='slow'
print(alien_0)

#Modifying existing values in dictionary
alien_0['color'] = 'yellow'

if alien_0['speed']=='slow':
    alien_0['x_incr']+=1
elif alien_0['speed']=='medium':
    alien_0['x_incr']+=2
elif alien_0['speed']=='fast':
    alien_0['x_incr']+=3

print(alien_0)

#Removing key value pairs
del alien_0['points']
print(alien_0)

#LOOPING THROUGH A DICTIONARY
#You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

user= {
 'username': 'Susan Smith',
 'first': 'Susan',
 'last': 'Smith',
 }
#Looping through key-value pairs
for x,y in user.items():      #items() returns a list of key-value pairs 
    print("\nKey: " + x)
    print("Value: " + y)

fav_lang = {
 'Sheryl': 'python',
 'Anju': 'c',
 'Edward': 'ruby',
 'Nadim': 'python',
 'Sai': 'python'
 }
#Looping through the keys
for x in fav_lang.keys():                   # default behavior when looping through a dictionary
    print(x)                                #keys() returns the list of keys
print("\n")                                

friends=['Edward','Sharon' ]
for x in fav_lang:
    if x in friends:
        print(f'{x} loves {fav_lang[x]}')   #Displays what language some specified people likes
#OR
for i in friends:
    if i in fav_lang.keys():
        print(f'{i} loves {fav_lang[i]}')

#Looping through the values
for i in fav_lang.values():         #values() method returns a list of values without any keys
    print(i)
print("")

#Use a set() to avoid repetition of values   ,A set is a list where each item is unique
for i in set(fav_lang.values()):
    print(i)
print("")

#Sorting keys in a dictionary
for i in sorted(fav_lang.items()):
    print(i)
print("")

#NESTING
#A LIST OF DICTIONARIES

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'pink', 'points': 15}
aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#Creating 10 blue aliens
alien=[]

for alnum in range(10):
    new={'color':'blue', 'points':10}
    alien.append(new)
print(f'Total number of aliens is {len(alien)}')

for i in alien[1:3]:
    if i['color']=='blue':
        i['color']='white'
        i['speed']='fast'
print(alien)

#A LIST IN A DICTIONARY

pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }

print(f"You ordered a {pizza['crust']}-crust pizza")
print(f"The toppings are:")
for i in pizza['toppings']:
    print(i+"\t")

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for i in favorite_languages.keys():
    print(f"{i}'s favorite languages are:")
    for j in favorite_languages[i]:
        print(j+"\t")

#DICTIONARY INSIDE A DICTIONARY

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
print(users['mcurie']['first'])
for i,j in users.items():
    print(f'Username:{i}')                #i represents set of keys and j represents the value(dictionaries inside)
    print(f'Full Name:{j["first"].title()+" "+j["last"].title()}')
    print(f'Location:{j["location"].title()}')

#Getting a dictionary from user

Voters={}                               #Create an empty dictionary
poll=True
while poll:
    name=input("Enter your name:")      #Collect the key
    age=int(input("Enter your age: "))  #Collect the value
    Voters[name]=age                    #Connect them 
    c=input("Do you want to continue? (y/n): ")
    if c=='n':
        poll=False

#Using function
def voterlist(name,age):
    Voters[name]=age
    return Voters
Voters={}
a=voterlist('Ashish',28)
print(a)