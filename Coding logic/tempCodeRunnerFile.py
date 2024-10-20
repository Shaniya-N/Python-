matrix=[]
print("Enter the 2D array row by row (press Enter without input to stop):")
while True:
    row_input = input()
    if row_input == "":  # Stop input when an empty line is entered
        break
    row = list(map(int, row_input.split()))  # Convert each row's input to a list of integers
    matrix.append(row)

print(matrix)