# Find the largest number from a set of numbers
s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    s.append(int(input()))
l=s[0]
for i in s:
    if i>l:
        l=i
print(f"The largest number is {l}")

'''
O/P:
    Count of numbers:5
    Enter the numbers:
    23
    65
    01
    30
    -92
    The largest number is 65
'''
    
s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    s.append(int(input()))
print(max(s))



s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    s.append(int(input()))
largest=float('-inf')
for i in s:
    if i>largest:
        largest=i
print(largest) 



