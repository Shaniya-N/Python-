# Find the largest number from a set of numbers
s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    x=int(input())
    s.append(x)
l=s[0]
for i in range(n):
    if s[i]>l:
        l=s[i]
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
    





