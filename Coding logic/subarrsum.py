# Python function that returns all sublists (or subsets) of a given list whose
# elements sum up to the target sum

a=input().split()
a=list(map(int,a))
n=int(input())
l=len(a)

def sub(a,n):
    c=[]
    for i in range(l):
        sum=a[i]
        b=[a[i]]
        for j in a:
            while sum<n:
                b.append(j)
                sum+=j
                if sum==n:
                    c.append(b)
    return c
y=sub(a,n)
for i in y:
    print(i)