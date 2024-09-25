# Find the 2nd smallest number from the list
a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    x=int(input())
    a.append(x)

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