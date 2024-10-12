#Find the immediate palindrome larger than the given number


def ispalindrome(a):
    if a[:]==a[::-1] and len(a)>1:
        return True
    
def findpalindromic(a):
    while True:
        a=a+1
        num=str(a)
        if ispalindrome(num):
            return int(num)
    
a=int(input())
result=findpalindromic(a)
print(result)