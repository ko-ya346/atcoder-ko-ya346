import networkx as nx
import matplotlib.pyplot as plt


g = nx.fast_gnp_random_graph(8, 0.26, 1)
print(nx.dijkstra_path(g, 0, 2))

nx.draw(g)
plt.show()

