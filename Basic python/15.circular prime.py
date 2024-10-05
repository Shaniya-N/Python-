# Check if a number is circular prime or not
# A circular prime is a prime number that remains prime under any cyclic rotation of its digits.
# For example, 197 is a circular prime because 197, 971, and 719 are all prime numbers.
# When checking for circular primes, only the left rotations are considered.

def isprime(n):
    if n==0 or n==1:
        return True
    else:
        for i in range(2,int(n/2)):
            if n%i==0:
                return False
        return True

def rotate(n):
    flag=1
    for i in range(len(str(n))):
        n=str(n)[i:]+str(n)[:i]
        if isprime(int(n)):
            continue
        else:
            flag=0
            break
    return flag

n=int(input("Enter the number:"))
flag=rotate(n)
if flag==1:
    print(f"It is a circular prime")
else:
    print(f"It is not a circular prime")
