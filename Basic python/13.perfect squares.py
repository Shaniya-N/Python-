# Check if a number is perfect square
import math
n=int(input("Enter the number:"))
r=int(math.sqrt(n))

if r*r==n:
    print(f"It is a perfect square\nSquare root={math.sqrt(n)}")
else:
    print("It is not a perfect square")