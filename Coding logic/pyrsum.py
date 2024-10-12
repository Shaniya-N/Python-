# Find the pyramid sum of the given list.Pyramid sum is calculated by repeated addition of
# consecutive numbers until the list has one element.
# Input: [1,2,3]
# Output: 8
# Explanation: [1,2,3]->[1+2,2+3]->[3+5]->[8]


def pyramidsum(a):
    while len(a) > 1:
        b=[]
        for i in range(len(a)-1):
            b.append(a[i]+a[i+1])
        a=b
    return a

a=input().split(',')
a=list(map(int,a))
sum=pyramidsum(a)
print(sum)