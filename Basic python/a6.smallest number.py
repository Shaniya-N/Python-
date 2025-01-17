#  Find the smallest number from the list

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))

s=float('inf')
for i in a:
    if i<s:
        s=i

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