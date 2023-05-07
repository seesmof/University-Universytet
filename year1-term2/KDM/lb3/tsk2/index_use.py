# Define the graph as a list of edges
graph1 = [(1, 2, 4), (1, 3, 3), (1, 4, 2), (2, 5, 2), (2, 7, 1), (3, 5, 6), (3, 6, 7), (4, 6, 2), (4, 7, 7),
          (5, 8, 4), (5, 9, 7), (6, 8, 4), (6, 10, 3), (7, 9, 5), (7, 10, 5), (8, 11, 4), (9, 11, 1), (10, 11, 3)],
graph2 = [(1, 2, 1), (1, 3, 3), (1, 4, 4), (2, 5, 2), (2, 7, 6), (3, 5, 5), (3, 6, 1), (4, 6, 4), (4, 7, 2),
          (5, 8, 7), (5, 9, 3), (6, 8, 3), (6, 10, 1), (7, 9, 4), (7, 10, 1), (8, 11, 2), (9, 11, 4), (10, 11, 5)]

# Ask the user for the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

# Create a list of vertices
vertices = []
for i in range(1, num_vertices + 1):
    vertices.append(i)

# Create a list of edges from the graph
edges = []
for edge in graph1:
    edges.append(edge)

# Sort the edges by weight in ascending order
edges = sorted(edges, key=lambda x: x[2])

# Create a list of sets for each vertex
sets = []
for vertex in vertices:
    sets.append({vertex})


# Define a function to find the set that contains a given vertex
def find_set(vertex):
    for set in sets:
        if vertex in set:
            return set


# Define a function to merge two sets
def merge_sets(set1, set2):
    sets.remove(set1)
    sets.remove(set2)
    sets.append(set1.union(set2))


# Initialize the minimum spanning tree
minimum_spanning_tree = []

# Iterate over the sorted edges
for edge in edges:
    # Find the sets that contain the vertices of the edge
    set1 = find_set(edge[0])
    set2 = find_set(edge[1])
    # If the sets are different, add the edge to the minimum spanning tree and merge the sets
    if set1 != set2:
        minimum_spanning_tree.append(edge)
        merge_sets(set1, set2)

# Display the minimum spanning tree
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} == {edge[2]}")

# Define a function to find the shortest path between two vertices


def shortest_path(start_vertex, end_vertex, path=[]):
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    shortest = None
    for vertex in sets[start_vertex-1]:
        if vertex not in path:
            new_path = shortest_path(vertex, end_vertex, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


# Ask the user for the start and end vertices
start_vertex = int(input("Enter the start vertex: "))
end_vertex = int(input("Enter the end vertex: "))

# Find the shortest path
shortest_path = shortest_path(start_vertex-1, end_vertex-1)

# Display the shortest path
print(f"Shortest Path: {[vertex+1 for vertex in shortest_path]}")
