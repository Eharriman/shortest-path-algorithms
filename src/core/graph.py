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
        if not self.directed
            self.adj[v].append((u, weight))

    def get_neighbours(self, u):
        return self.adj[u]