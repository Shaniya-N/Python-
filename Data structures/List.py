# LIST
# A list is a collection of items in a particular order.
# The items in your list don’t have to be related in any particular way. 
# Square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

listy=[2222,"girl","book",[56,92],[],"234"]
print(listy)        #[2222, 'girl', 'book', [56, 92], [], '234']


# ACCESSING ELEMENTS
# Lists are ordered collections, so you can access any element in a list by its position,
# or index, of the item desired.

print(listy[1])     #2nd element       girl
print(listy[-1])    #last element      234 


#MODIFYING ELEMENTS IN THE LIST

#Adding elements to list
listy[0]=3333    #Using index         
print(listy)     #[3333, 'girl', 'book', [56, 92], [], '234']

print(listy.append("door")) #appends an element to the end of the list    
                            #[[3333, 'girl', 'book', [56, 92], [], '234', 'door']

print(listy.insert(3,"window")) #inserts an element at a specified index
                                #[3333, 'girl', 'book', 'window', [56, 92], [], '234', 'door']

#Removing elements from list

del listy[-2]   #removing from a specific index
print(listy)    #[3333, 'girl', 'book', 'window', [56, 92], [], 'door']

popped=listy.pop()     #returns the last element and removes it from the list
print(popped)          #door
print(listy)           #[3333, 'girl', 'book', 'window', [56, 92], []]

popped=listy.pop(3)    #returns and removes element from the specific index
print(popped)          #window
print(listy)           #[3333, 'girl', 'book', [56, 92], []]

listy.remove(3333)     #removing an item by its value (removes only the first occurrence)
print(listy)           #['girl', 'book', [56, 92], []]

listy.clear()          #clear the whole list

# SORTING THE LIST

book=["Magic","Speed","Bad blood","Goblin"]

#sort() method
book.sort()                        #permanently sorts the list in alphabetic or numeric order(for homogenous lists)
print(book)                        #['Bad blood', 'Goblin', 'Magic', 'Speed']

book.sort(reverse=True)            #permanently sorts in reverse order
print(book)                        #['Speed', 'Magic', 'Goblin', 'Bad blood']

listy.sort(key=str)                #permanently sorting a heterogenous list based on str values
print(listy)                       #[[56, 92], [], 'book', 'girl']

print(book.sort())                 #prints none as sort() doesn't return any value

movies=["Old dads","Bruce almighty","Shutter island","Star wars"]

#sorted() function
print(sorted(movies))                #Temperorily sorting the list using sorted() function   
                                     #['Bruce almighty', 'Old dads', 'Shutter island', 'Star wars']      
print(sorted(movies,reverse=True))   #In reverse order       
                                     #['Star wars', 'Shutter island', 'Old dads', 'Bruce almighty']

#LOOPING THROUGH LISTS

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:        #For every magician in the list of magicians, print the magician’s name.
    print(magician)               #alice 
                                  # david 
                                  # carolina

# range() to make a list

numbers=list(range(10))
print(numbers)                    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers=list(range(1,11,2))
print(numbers)                    #[1, 3, 5, 7, 9]

#Creating a list using a for loop

sqrs=[]
for i in range(10):
    sqrs.append(i*i)
print(sqrs)                  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(min(sqrs))             #0
print(max(sqrs))             #81
print(sum(sqrs))             #285

#Creating list using for loop in a single line
sqrs=[i*i for i in range(10)]
print(sqrs)                   #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#SLICING
names=["Renuka", "Sheryl", "Anju", "Gopika", "Alvin", "Ben"]
print(names)                  #prints the entire list
print(names[:])               #prints the entire list
print(names[0:3])             #prints from zeroth position to second position
print(names[:2])              #zeroth and first
print(names[1:])              #first to last position
print(names[3])               #third item
print(names[::2])             #Zeroth second and fourth items
print(names[::-1])            #whole list in reverse order
print(names[-3:])             #last three items

#Loop through slices
for p in names[:3]:
    print(p)

#Getting a list from the user

n=int(input("Number of items:"))
heights=[]
for i in range(n):
    heights.append(input(""))
print(heights)
 

#Checking if a list is empty

items=["mango","banana","grape","apple"]
if items:
    print("Fruits are available")
else:
    print("The store room is empty")