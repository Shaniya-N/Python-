# To check whether a number is fibonacci or not
import  math

def isperfectsqr(n):
    if int(math.sqrt(n))**2 == n:
        return True
    
def fibonacci(n):
    if isperfectsqr(5*n*n+4) or isperfectsqr(5*n*n-4):
        return True

n=int(input("Enter a number:"))
if fibonacci(n):
    print("It is a fibonacci number")
else:
    print("It is not a fibonacci number")

