from collections import defaultdict

class Graph:
    def __init__(self, directed=True):
        self.adj = defaultdict(list)
        self.nodes = set()
        self.directed = directed

    def add_edge(self, u, v, weight):
        self.adj[u].append((v, weight))
        self.nodes.add(u)
        self.nodes.add(v)
        if not self.directed:
            self.adj[v].append((u, weight))

    def get_neighbours(self, u):
        return self.adj[u]



"""
graph1 = Graph(directed=True)

graph1.add_edge('A', 'B', 3)
graph1.add_edge('A', 'C', 5)
graph1.add_edge('B', 'C', 6)
graph1.add_edge('C', 'D', 2)

for neighbour, weight in graph1.get_neighbours('A'):
    print(f"Edge A -> {neighbour}, weight = {weight}")

for neighbour, weight in graph1.get_neighbours('B'):
    print(f"Edge B -> {neighbour}, weight = {weight}")

"""