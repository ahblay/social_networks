from basic_example import Network
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint as pp


nw = Network(45)
nw.init_normal_nodes()
for i in range(0, 100, 10):
    nw.simulate_interactions(i)

    structure = nw.get_structure()
    pp(structure)
    nodes = structure["nodes"]
    edges = structure["edges"]

    # Build your graph
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # Plot it
    nx.draw(G, with_labels=True)
    plt.show()
