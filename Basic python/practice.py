
a=int(input())
b=int(input())
print(str(a)[b])

a=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))
s1,s2=float('inf'),float('inf')
for i  in a:
    if i<s1:
        s1,s2=i,s1

print(a[1])