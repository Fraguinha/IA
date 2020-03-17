import networkx as nx
import csv
import matplotlib.pyplot as plt

with open("portugal.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    G = nx.Graph()
    for row in csv_reader:
        G.add_edge(row[0], row[1], weight=int(row[2]))


"""
Dividir os distritos em 3 regiões: Norte, Centro e Sul
Calcular distancia 'media' entre 2 distritos pertencentes:
-mesma região
-regiões adjacentes
-regiões opostas
"""

N = [
    "vianadocastelo",
    "braga",
    "braganca",
    "vilareal",
    "porto",
    "aveiro",
    "viseu",
    "guarda",
]
C = ["coimbra", "castelobranco", "leira", "santarem", "portalegre", "lisboa"]
S = ["setubal", "evora", "beja", "faro"]


def h(origin, destination):
    if (
        origin
        and destination in N
        or origin
        and destination in C
        or origin
        and destination in S
    ):
        return 180
    elif origin in N and destination in S or origin in S and destination in N:
        return 540
    else:
        return 290


origin = input("Origem: ")
destination = input("Destino: ")

path = nx.astar_path(G, origin, destination, h)
print(path)
