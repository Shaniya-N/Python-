#  Find the LCM of 2 numbers
# LCM formula: The LCM is computed by dividing the product of the two numbers by their GCD.

import math
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
lcm=abs((n*m)//math.gcd(n,m))
print(lcm)