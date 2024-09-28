#  an immutable list is called a tuple

dimensions = (200, 50)
for dimension in dimensions:
 print(dimension)

dimension[0]=345    #ERROR
#Writing over a tuple
dimensions=(233,900) #The entire tuple can be redefined
