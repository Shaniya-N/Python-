s=[]
n=int(input("Count of numbers:"))
print("Enter the numbers:")
for i in range(n):
    s.append(int(input()))
print(max(s))