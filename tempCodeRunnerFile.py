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