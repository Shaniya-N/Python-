# Find the position of a given digit in a number
try:
    n=int(input("Number"))
    d=int(input("digit"))
    #1.By traversing through the number string
    for i in range(len(str(n))):
        if str(n)[i]==str(d):
            print(f"pos={i}")
    #2.By using find method
    print(str(n).find(d))

except ValueError:
    print("Invalid input")  #should not accept if the input is not a number