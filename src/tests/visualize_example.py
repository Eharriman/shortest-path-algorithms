from src.core.graph import Graph
from src.visual.graph_visual import GraphVisualizer

graph = Graph(directed=True)
graph.add_edge('A', 'B', 3)
graph.add_edge('B', 'C', 1)
graph.add_edge('A', 'C', 7)

graph_plot = GraphVisualizer(graph)

graph_plot.draw(title="Test graph image")