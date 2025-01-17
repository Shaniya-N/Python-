# while True:
#     try:
#         n=int(input("Number"))
#         d=int(input("digit"))
#         a=str(n)
#         if d<len(a):
#          print(a[d])
#         else:
#            print("NPPPP")
#     except ValueError:
#         print("Invalid input")

# a=[]
# n=int(input("how many"))
# for i in range(n):
#     a.append(int(input()))
# l=a[0]
# for i in a:
#     if i>l:
#         l=i
# print(l)




# # Happy numbers
# def sumofdig(n):
#     sum=0
#     while n>0:
#         d=n%10
#         sum+=d
#         n=n//10
#     return sum
# n=int(input())
# while True:
#     a=sumofdig(n)
#     print(a)
#     if a<9:
#         print("Happyyy")
#         break
#     else:
#         n=a

#Non repeating character
'''s=input()
for i in s:
    a=s.index(i)
    if i not in s[a+1:]:
        print(a)
        break'''

# Alice and Bob

'''num=list(map(int,input().split()))
arr=[]
while num:
    a1=min(num)
    num.remove(a1)
    b1=min(num)
    num.remove(b1)
    arr.extend([b1,a1])
print(arr)'''

# Pangram

'''s=set(input())
if len(s)==26:
    print("Yeeppp")
else:
    print("Noppp")'''

# Sentences word count
'''s=list(input().split(","))
w=[]
for i in s:
    w.append(i.count(" ")+1)
print(w)
print(max(w))'''

#count of digits that divide a number

'''n=int(input())
a,c=n,0
while n>0:
    d=n%10
    if a%d==0:
        c+=1
    n=n//10
print(c)'''

# First palindrome
'''s=input().split(",")
flag=0
for i in s:
    if i==i[::-1]:
        print(i)
        flag=1
        break
if flag==0:
    print("NOOOOOO")'''


# Employee working hours
s=list(map(int,input().split()))
n=int(input())
c=0
for i in s:
    if i>=n:
        c+=1
print(c)

# Digit sum and element sum

s=list(map(int,input().split()))
sumo=sum(s)
dsumo=0
for i in s:
    while i>0:
        d=i%10
        dsumo+=d
        i=i//10
print(abs(dsumo-sumo))

#Triangle

a=int(input())
b=int(input())
c=int(input())
if a+b>c:
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isoceles")
    else:
        print("Scalene")
else:
    print("None")






















