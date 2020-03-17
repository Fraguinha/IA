import networkx as nx
import csv
import matplotlib.pyplot as plt

with open("portugal.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    G = nx.Graph()
    for row in csv_reader:
        G.add_edge(row[0], row[1], weight=row[2])

origin = input("Origem: ")
destination = input("Destino: ")

S = nx.bfs_successors(G, origin, None)
L = list(S)


def BFS(L, origin, destination, path):
    while origin != destination:
        for el, li in L:
            if destination in li:
                path.insert(0, el)
                destination = el
                break
    return path


path = BFS(L, origin, destination, [destination])
print(path)


def calc_distance(G, path):
    sum = 0
    for i in range(len(path) - 1):
        sum += int(G[path[i]][path[i + 1]]["weight"])
    return sum


print(calc_distance(G, path))
# nx.draw(nx.bfs_tree(G, origin, False, None))
# plt.show()
