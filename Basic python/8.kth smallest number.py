# Find the kth smallest number from the list

n=int(input("Count of numbers:"))
print("Enter the numbers:")
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
k=int(input("K:"))
a.sort()
print(f"Kth smallest:{a[k-1]}")      

'''
O/P:
    Count of numbers:3
    Enter the numbers:
    8
    23
    1
    K:2
    Kth smallest:8
'''