# Find the 2nd largest number from a list of numbers

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))

a.sort()
print(f"Second largest:{a[-2]}")

'''
O/P:
    Count of numbers:3
    Enter the numbers:
    23
    54
    87
    Second largest:54
'''

#Second largest less then the largest element(say there are two elements with the same highest value)

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))
a=set(a)      
a.remove(max(a))
l=next(iter(a))      #The iter() function can create an iterator over the set, and next() fetches an arbitrary first element.
for i in a:
    if i>l:
      l=i
print(l)

# OR

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
a=set(int(input()) for i in range(n))
l,s=float('-inf'),float('-inf')
for i in a:
    if i>l:
        s,l=l,i
    elif l>i>s:
        s=i
print(s)
                                                    
# Reverse an array

n=int(input("size"))
a=[]
for i in range(n):
    a.append(i)
a=a[::-1]
print(a)

