# Step 1: Accept input from user
import heapq
num_vertices = int(input("Enter number of vertices: "))
graph = {}

for i in range(1, num_vertices+1):
    graph[i] = {}
    for j in range(i+1, num_vertices+1):
        weight = int(input(f"Enter weight between {i} and {j}: "))
        graph[i][j] = weight
        graph[j][i] = weight

# Step 2: Implement Dijkstra's Algorithm


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


# Step 3: Find shortest path using Dijkstra's Algorithm
start_vertex = int(input("Enter start vertex: "))
distances = dijkstra(graph, start_vertex)

# Step 4: Output shortest path
shortest_path = []
current_vertex = num_vertices
while current_vertex != start_vertex:
    shortest_path.append(str(current_vertex))
    current_vertex = min(graph[current_vertex], key=lambda x: distances[x])
shortest_path.append(str(start_vertex))
shortest_path.reverse()

print(" -> ".join(shortest_path))
