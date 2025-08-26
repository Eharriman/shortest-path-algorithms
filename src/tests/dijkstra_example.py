from src.core.graph import Graph
from src.core.dijkstra import dijkstra
from src.visual.graph_visual import GraphVisualizer

"""
graph1 = Graph(directed=True)

graph1.add_edge('A', 'B', 4)
graph1.add_edge('A', 'C', 8)
graph1.add_edge('B', 'E', 6)
graph1.add_edge('C', 'D', 2)
graph1.add_edge('D', 'E', 10)
"""
"""
graph1 = Graph(directed=True)
graph1.add_edge('A', 'B', 2)
graph1.add_edge('A', 'F', 5)
graph1.add_edge('A', 'L', 8)
graph1.add_edge('B', 'C', 7)
graph1.add_edge('B', 'D', 8)
graph1.add_edge('C', 'E', 11)
graph1.add_edge('D', 'E', 4)
graph1.add_edge('D', 'H', 3)
graph1.add_edge('D', 'G', 6)
graph1.add_edge('D', 'J', 2)
graph1.add_edge('F', 'I', 12)
graph1.add_edge('I', 'J', 9)
graph1.add_edge('I', 'K', 2)


The answer should be:
A -> B: 2
A -> C: 9
A -> D: 10
A -> E: 14
A -> H: 13
A -> G: 16
A -> F: 5
A -> I: 17
A -> J: 12
A -> K: 19
A -> L: 8
"""

graph1 = Graph(directed=True)
graph1.add_edge('A', 'B', 3)
graph1.add_edge('A', 'C', 7)
graph1.add_edge('B', 'C', 1)

"""
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
graph1.add_edge('H', 'N', 5)
graph1.add_edge('I', 'N', 1)
graph1.add_edge('E', 'J', 4)
graph1.add_edge('J', 'I', 2)
graph1.add_edge('J', 'L', 2)
graph1.add_edge('L', 'O', 3)
graph1.add_edge('L', 'U', 5)
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
"""


visualizer = GraphVisualizer(graph1)

dist, prev = dijkstra(graph1, 'A', visualizer)

print("Distances:", dist)
print("Previous:", prev)
