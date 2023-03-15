# function to check if (2a - b) is divisible by 3
def check_relation(a, b):
    return (2*a - b) % 3 == 0


# take input from the user for two sets
setA = set(map(int, input("Enter elements of set A separated by space: ").split()))
setB = set(map(int, input("Enter elements of set B separated by space: ").split()))

# initialize an empty matrix with the dimensions of the two sets
matrix = [[0 for j in range(len(setB))] for i in range(len(setA))]

# fill in the matrix with 1s and 0s based on whether the relation holds between the corresponding elements
for i, a in enumerate(setA):
    for j, b in enumerate(setB):
        if check_relation(a, b):
            matrix[i][j] = 1

# display the binary relation matrix
print("Binary Relation Matrix:")
for row in matrix:
    print(row)
