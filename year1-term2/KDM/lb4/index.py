import networkx as nx

# create a directed weighted graph
G = nx.DiGraph()

# add nodes to the graph
G.add_nodes_from(['1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', '11', '12', '13'])

# add edges to the graph
G.add_edge('1', '2', capacity=11)
G.add_edge('1', '3', capacity=15)
G.add_edge('1', '4', capacity=11)
G.add_edge('1', '5', capacity=15)
G.add_edge('2', '6', capacity=7)
G.add_edge('2', '7', capacity=9)
G.add_edge('3', '6', capacity=4)
G.add_edge('4', '7', capacity=8)
G.add_edge('4', '8', capacity=9)
G.add_edge('4', '9', capacity=4)
G.add_edge('5', '8', capacity=9)
G.add_edge('5', '9', capacity=5)
G.add_edge('6', '10', capacity=8)
G.add_edge('7', '10', capacity=13)
G.add_edge('7', '11', capacity=7)
G.add_edge('8', '11', capacity=4)
G.add_edge('8', '12', capacity=4)
G.add_edge('9', '12', capacity=12)
G.add_edge('10', '13', capacity=20)
G.add_edge('11', '13', capacity=10)
G.add_edge('12', '13', capacity=13)

# find the full flow
full_flow = nx.maximum_flow_value(G, '1', '13')

# find the maximum flow
max_flow_value, max_flow_dict = nx.maximum_flow(G, '1', '13')

# print the full and maximum flows
print("Full flow:", full_flow)
print("Maximum flow:", max_flow_value)
