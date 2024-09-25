# Find a digit at a specific place in a number

n=input("Number:")
x=int(input("Index:"))

if x<len(n):
    print(n[x])
else:
    print("Invalid")

'''
O/P:
    Number:23443267
    Index:5
    2
'''
