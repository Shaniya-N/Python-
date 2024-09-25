# Find the kth largest number from a list of numbers

s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:") 
for i in range(n):
    x=int(input())
    s.append(x)
k=int(input("k:"))
s.sort()
print(f"Kth largest:{s[len(s)-k]}")

'''
O/p:
    Count of numbers:3
    Enter the numbers:
    78
    43
    21
    k:2
    Kth largest:43
'''