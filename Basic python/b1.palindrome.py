#  Is the given number a palindrome?

n=int(input("Enter the number:"))
s=str(n)
if  s[::-1]==s:
    print("Yes")
else:
    print("No")

# OR
n=int(input("Enter the number:"))
r=n
res=0
while(r>0):
    digit=r%10
    res=res*10+digit
    r=r//10

if str(res)==str(n):
     print("Yes")
else:
     print("No")
