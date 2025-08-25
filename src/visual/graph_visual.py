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

    def draw(self, highlight_nodes=None, highlight_edges=None, title="Test Graph", pause=None, node_labels=None):
        pos = nx.spring_layout(self.G, seed=42)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')

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

        plt.figure(figsize=(10, 7))
        nx.draw(self.G, pos, with_labels=True, node_color=node_colours, edge_color=edge_colours, node_size=1000,
                font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        if node_labels:
            custom_labels = {
                node: f"{node}\n{int(node_labels[node]) if node_labels[node] < float('inf') else '∞'}"
                for node in self.G.nodes
            }
            nx.draw_networkx_labels(self.G, pos, labels=custom_labels, font_color='white')

        plt.title(title)
        plt.tight_layout()
        plt.show(block=False)

        if pause:
            plt.pause(pause)
            plt.close()
        else:
            plt.show()

