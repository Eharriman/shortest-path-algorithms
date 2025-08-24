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
        pos = nx.spring_layout(self.G, seed=42)
        edge_lables = nx.get_edge_attributes(self.G, 'weight')

        node_colours = []
        for node in self.G.nodes:
            if highlight_nodes and node in highlight_nodes:
                node_colours.append('green')
            else:
                node_colours.append('blue')

        edge_colours = []
        for edge in self.G.edges:
            if highlight_edges and edge in highlight_edges:
                edge_colours.append('red')
            else:
                edge_colours.append('grey')

