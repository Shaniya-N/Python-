#  Is the given number a palindrome?

n=int(input("Enter the number:"))
s=str(n)
if  s[::-1]==s:
    print("Yes")
else:
    print("No")