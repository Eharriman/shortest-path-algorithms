import networkx as nx
import matplotlib.pyplot as plt
from src.core.graph import Graph

class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph
        self.G = nx.DiGraph() if graph.directed else nx.Graph()
        self._convert_graph()

    def _convert_graph(self):
        for u in self.graph.nodes:
            self.G.add_node(u)
        for u in self.graph.nodes:
            for v, w in self.graph.get_neighbours(u):
                self.G.add_edge(u, v, weight=w)

    def draw(self, highlight_nodes=None, highlight_edges=None, title="Test Graph", pause=None):
        pass
