def is_subset(arr1, arr2):
    # Convert both arrays to sets
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Check if set2 is a subset of set1
    return set2.issubset(set1)

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4]

if is_subset(arr1, arr2):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")


