from queue import PriorityQueue

# define the Kruskal's algorithm function


def kruskal(graph, num_vertices):
    # initialize the minimum spanning tree and the parent array
    mst = []
    parent = [i for i in range(num_vertices)]

    # define the find function for the union-find algorithm
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # sort the edges by weight
    edges = []
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))
    edges.sort()

    # iterate over the edges and add them to the MST if they don't create a cycle
    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            mst.append(edge)
            parent[find(u)] = find(v)

    return mst

# define the Dijkstra's algorithm function


def dijkstra(graph, start):
    # initialize the distances and the priority queue
    distances = {i: float('inf') for i in range(len(graph))}
    distances[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))

    # iterate over the vertices and update the distances
    while not pq.empty():
        current_distance, current_vertex = pq.get()
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight != 0:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    pq.put((distance, neighbor))

    return distances


# get the number of vertices and the weights from the user
num_vertices = int(input("Enter the number of vertices: "))
graph = []
for i in range(num_vertices):
    row = list(
        map(int, input(f"Enter the weights for vertex {i+1}: ").split()))
    graph.append(row)

# find the minimum spanning tree using Kruskal's algorithm
mst = kruskal(graph, num_vertices)
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[1]} -- {edge[2]}: {edge[0]}")

# find the shortest path using Dijkstra's algorithm
start = int(input("Enter the starting vertex for Dijkstra's algorithm: "))
distances = dijkstra(graph, start)
print("Shortest Path:")
for i in range(num_vertices):
    if i != start:
        print(f"{start} -- {i}: {distances[i]}")
