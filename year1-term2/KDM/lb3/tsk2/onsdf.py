import networkx as nx
import matplotlib.pyplot as plt

G1 = [["e1", 1, 2], ["e2", 1, 3], ["e3", 3, 4], ["e4", 2, 4]]
G2 = [["e4", 2, 4], ["e5", 2, 3], ["e6", 3, 5], ["e7", 4, 5]]

nx_G1 = nx.Graph()
nx_G1.add_edges_from([(str(x[1]), str(x[2])) for x in G1])

nx_G2 = nx.Graph()
nx_G2.add_edges_from([(str(x[1]), str(x[2])) for x in G2])

plt.subplot(131)
nx.draw(nx_G1, with_labels=True)
plt.title('Graph G1')

plt.subplot(132)
nx.draw(nx_G2, with_labels=True)
plt.title('Graph G2')

plt.subplot(133)
nx_G_union = nx.Graph()
nx_G_union.add_edges_from([(str(x[1]), str(x[2])) for x in G1])
nx_G_union.add_edges_from([(str(x[1]), str(x[2])) for x in G2])
nx.draw(nx_G_union, with_labels=True)
plt.title('Union of G1 and G2')

plt.show()
