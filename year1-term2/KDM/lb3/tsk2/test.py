# Kruskal's Algorithm for finding Minimum Spanning Tree

# Graph represented as list of edges with weights
import heapq

# Ask the user for the number of vertices in the graph
num_vertices = int(input("Введіть кількість вершин: "))

# Create an empty dictionary to represent the graph
graph = {}

# For each vertex in the graph
for i in range(1, num_vertices+1):
    # Create a sub-dictionary to represent the edges and weights for that vertex
    edges = {}
    # For each other vertex in the graph
    for j in range(1, num_vertices+1):
        # If the other vertex is not the current vertex
        if i != j:
            # Ask the user for the weight of the edge between the current vertex and the other vertex
            weight = int(
                input(f"Введіть вагу між {i} та {j}: "))
            # If the weight is not 0, add the other vertex and its weight to the sub-dictionary for the current vertex
            if weight != 0:
                edges[j] = weight
    # Add the sub-dictionary for the current vertex to the graph dictionary
    graph[i] = edges

# Sort edges by weight
graph_edges = []
for i in range(1, num_vertices+1):
    for j, weight in graph[i].items():
        graph_edges.append((i, j, weight))
graph_edges = sorted(graph_edges, key=lambda x: x[2])

# Initialize parent dictionary and rank dictionary for union-find algorithm
parent = {i: i for i in range(1, num_vertices+1)}
rank = {i: 0 for i in range(1, num_vertices+1)}


# Define find and union functions for union-find algorithm
def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1


# Initialize variables for minimum spanning tree and total weight
minimum_spanning_tree = []
total_weight = 0

# Iterate through edges and add to minimum spanning tree if they don't create a cycle
for edge in graph:
    node1, node2, weight = edge
    if find(node1) != find(node2):
        union(node1, node2)
        minimum_spanning_tree.append(edge)
        total_weight += weight

# Print minimum spanning tree and total weight
print(f"\nМінімальне остовне дерево:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} = {edge[2]}")
print(f"\nВага мінімального остовного дерева: {total_weight}")

# Shortest path using Dijkstra's Algorithm


# Dijkstra's Algorithm for finding shortest path
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (distance, current_node) = heapq.heappop(heap)
        if distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance_to_neighbor = distance + weight
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                heapq.heappush(heap, (distance_to_neighbor, neighbor))
    path = [end]
    current_node = end
    while current_node != start:
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] == distances[neighbor] + weight:
                path.append(neighbor)
                current_node = neighbor
                break
    path.reverse()
    return path


# Print shortest path
shortest_path = dijkstra(graph, 1, 11)
shortest_path = shortest_path.replace("[", "")
shortest_path = shortest_path.replace("]", "")
print(f"Найкоротший шлях: {shortest_path}\n")
