# Find sum of 'n' numbers

n=int(input("Enter the limit:"))
s=0
for i in range(1,n+1):
    s+=i
print(f"Sum is {s}")