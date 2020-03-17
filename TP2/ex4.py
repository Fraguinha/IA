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

D = nx.dfs_successors(G, origin, None)


def DFS(D, origin, destination, path):
    for key in D:
        path.append(key)
        if destination in D[key]:
            path.append(destination)
            return path
        flag = True
        for v in D[key]:
            if v in D.keys():
                flag = False
        if flag:
            for i in reversed(path):
                if len(D[i]) <= 1:
                    path.remove(i)
                else:
                    break


path = DFS(D, origin, destination, [])
print(path)


def calc_distance(G, path):
    sum = 0
    for i in range(len(path) - 1):
        sum += int(G[path[i]][path[i + 1]]["weight"])
    return sum


print(calc_distance(G, path))
