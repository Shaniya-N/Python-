# Find the kth largest number from a list of numbers

s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
k=int(input("k:")) 
for i in range(n):
    x=int(input())
    s.append(x)

s.sort()
print(f"Kth largest:{s[len(s)-k]}")

'''
O/p:
    Count of numbers:3
    Enter the numbers:
    k:2
    56
    78
    32
    Kth largest:56
'''