# define a function to check if a pair is in the relation
def is_related(a, b):
    return (2*a - b) % 3 == 0


# get input from user for set A
print("")
set_a = input("Enter set A elements: ").split()
set_a = [int(a) for a in set_a]

# get input from user for set B
set_b = input("Enter set B elements: ").split()
set_b = [int(b) for b in set_b]

# create a list of tuples for all pairs that are related
related_pairs = [(a, b) for a in set_a for b in set_b if is_related(a, b)]

# create a binary relation matrix as a dictionary of lists
relation_matrix = {}
for a in set_a:
    relation_matrix[a] = []
    for b in set_b:
        if (a, b) in related_pairs:
            relation_matrix[a].append(1)
        else:
            relation_matrix[a].append(0)

# output the binary relation matrix
print("\nBinary relation matrix:")
print("   ", end="")
for b in set_b:
    print(f"{b} ", end="")
print()
for a in set_a:
    print(f"{a} |", end="")
    for i in range(len(set_b)):
        print(f"{relation_matrix[a][i]} ", end="")
    print()

# calculate and output the symmetric difference of A and B
symmetric_difference = set(set_a) ^ set(set_b)
print("\nSymmetric difference of A and B:", symmetric_difference)
print("")
