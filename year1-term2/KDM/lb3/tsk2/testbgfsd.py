# Kruskal's algorithm for finding minimum spanning tree
# The program asks for the number of vertices and the weight of each edge
# If the weight is 0, the edge is not added to the graph
# The program outputs the minimum spanning tree, shortest path, and weight of the minimum spanning tree
# The program is written in Python

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_minimum_spanning_tree(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

    def shortest_path(self, start, end):
        visited = [False] * self.V
        distances = [float('inf')] * self.V
        distances[start] = 0
        path = [-1] * self.V

        for i in range(self.V - 1):
            min_distance = float('inf')
            for j in range(self.V):
                if visited[j] == False and distances[j] < min_distance:
                    min_distance = distances[j]
                    u = j

            visited[u] = True

            for v, w in enumerate(self.graph[u]):
                if visited[v] == False and w != 0 and distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
                    path[v] = u

        shortest_path = []
        u = end
        while path[u] != -1:
            shortest_path.insert(0, u)
            u = path[u]
        shortest_path.insert(0, u)

        return shortest_path


# main program
V = int(input("Enter the number of vertices: "))
g = Graph(V)

for i in range(V):
    weights = list(
        map(int, input(f"Enter the weights for edges from vertex {i}: ").split()))
    for j in range(V):
        if weights[j] != 0:
            g.add_edge(i, j, weights[j])

# minimum spanning tree
mst = g.kruskal_minimum_spanning_tree()
print("Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v} = {weight}")
mst_weight = sum(weight for u, v, weight in mst)
print(f"Weight of minimum spanning tree: {mst_weight}")

# shortest path
start = 0
end = V - 1
shortest_path = g.shortest_path(start, end)
print("Shortest Path:")
print("->".join(str(vertex) for vertex in shortest_path))
