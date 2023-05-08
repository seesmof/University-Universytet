class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (truly uses path compression technique)
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Variable to store the edges of the minimum spanning tree
        mst = []

        # Variable to keep track of the number of edges added to the minimum spanning tree
        e = 0

        # Number of edges to be taken is less than V-1
        while e < self.V - 1:
            u, v, w = self.graph.pop(0)
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause cycle, then include it in result
            if x != y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the edges of the minimum spanning tree in the desired format
        for u, v, weight in mst:
            print("{} -- {} = {}".format(u, v, weight))


# Ask the user for the number of vertices in the graph
n = int(input("Enter the number of vertices: "))

# Create a Graph object with the given number of vertices
g = Graph(n)

# Ask the user for the weight between each vertex pair and add the edges to the graph object
for i in range(n):
    for j in range(i+1, n):
        weight = int(
            input("Enter the weight between {} and {}: ".format(i+1, j+1)))
        g.addEdge(i, j, weight)

# Call the kruskal method of the Graph object to find the minimum spanning tree
g.kruskal()
