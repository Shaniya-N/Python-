# Find the 2nd smallest number from the list
a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))

a.sort()
print(f"Second smallest:{a[1]}")

'''
O/P:
    Count of numbers:3
    Enter the numbers:
    45
    32
    12
    Second smallest:32
'''

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))

s1,s2=float('inf'),float('inf')
for i in a:
    if s1>i:
        s2,s1=s1,i
    elif s1>i>s2:
        s2=i
print(s2)


