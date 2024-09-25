# Find the number of occurences of a given digit in a number

def count(n,x):
    c=0
    number=str(n)
    for i in number:
        if x==int(i):
            c+=1
    return c

n=int(input("Enter the number:"))
x=int(input("Enter the requested digit:"))
c=count(n,x)
print(f"Count of {x} in {n} is {c}")

'''
O/P:
    Enter the number:5634343
    Enter the requested digit:3
    Count of 3 in 5634343 is 3
'''

# Find the count of digits in a number

n=int(input("Number:"))
print(len(str(abs(n))))

'''
O/P:
    Number:3455678
    7
'''