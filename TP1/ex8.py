# import matplotlib.pyplot as plt
import networkx as nx
import csv

csv = csv.reader(open("portugal.csv", "r"))

G = nx.Graph()

for line in csv:
    G.add_edge(line[0], line[1], weight=line[2])

for node in G.nodes():
    print(node + ":", end=" ")
    for neighbor in G.neighbors(node):
        print(neighbor, end=" ")
    print()

# nx.draw(G, with_labels=True, font_weight="bold")
# plt.savefig("graph.png")
# plt.show()
