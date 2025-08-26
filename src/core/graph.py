from collections import defaultdict

class Graph:
    def __init__(self, directed=True):
        self.adj = defaultdict(list)
        self.nodes = set()
        self.directed = directed

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

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

graph1 = Graph(directed=True)

graph1.add_edge('A', 'B', 2)
graph1.add_edge('A', 'C', 3)
graph1.add_edge('B', 'D', 5)
graph1.add_edge('B', 'E', 3)
graph1.add_edge('D', 'F', 1)
graph1.add_edge('D', 'G', 7)
graph1.add_edge('F', 'M', 6)
graph1.add_edge('G', 'H', 4)
graph1.add_edge('G', 'I', 3)
graph1.add_edge('H', 'M', 2)
graph1.add_edge('H', 'N', 1)
graph1.add_edge('E', 'J', 4)
graph1.add_edge('J', 'I', 2)
graph1.add_edge('J', 'L', 2)
graph1.add_edge('L', 'O', 3)
graph1.add_edge('L', 'U', 4)
graph1.add_edge('C', 'E', 6)
graph1.add_edge('C', 'P', 2)
graph1.add_edge('P', 'S', 3)
graph1.add_edge('P', 'R', 9)
graph1.add_edge('S', 'T', 6)
graph1.add_edge('T', 'U', 3)
graph1.add_edge('T', 'V', 7)
graph1.add_edge('A', 'W', 6)
graph1.add_edge('W', 'Q', 6)
graph1.add_edge('W', 'X', 3)
graph1.add_edge('W', 'Y', 5)
graph1.add_edge('Q', 'R', 2)
graph1.add_edge('X', 'Z', 2)
graph1.add_edge('Y', 'Z', 3)
graph1.add_edge('Z', 'V', 5)