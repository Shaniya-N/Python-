#  Find the smallest number from the list

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    x=int(input())
    a.append(x)

s=a[0]
for i in range(n):
    if a[i]<s:
        s=a[i]

print(f"Smallest number:{s}")

'''
O/P:
    Count of numbers:3
    Enter the numbers:
    23
    54
    1
    Smallest number:1
'''