# Find the 2nd largest number from a list of numbers

s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    x=int(input())
    s.append(x)

s.sort()
print(f"Second largest:{s[len(s)-2]}")

'''
O/P:
    Count of numbers:3
    Enter the numbers:
    23
    54
    87
    Second largest:54
'''

s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    x=int(input())
    s.append(x)
s=list(set(s))
s.remove(max(s))
l=s[0]
for i in range(len(s)):
    if s[i]>l:
        l=s[i]
print(l)
