#  Rotate the digits in a number

def rotate(num,dir,pos):
    if dir==0:
        print(f"After rotation:{num[pos:]+num[:pos]}")
    else:
        print(f"After rotation:{num[-pos:]+num[:-pos]}")
        
num=input("Enter the number:")
dir=int(input("Choose left(0) or right(1):"))
pos=int(input("Number of places to rotate:"))
rotate(num,dir,pos)




