from src.core.graph import Graph
from src.core.bellman_ford import bellman_ford

graph1 = Graph(directed=True)
"""
graph1.add_edge('A', 'B', 4)
graph1.add_edge('A', 'C', 8)
graph1.add_edge('B', 'E', 6)
graph1.add_edge('C', 'D', 2)
graph1.add_edge('D', 'E', 10)

"""

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

result = bellman_ford(graph1, 'A')

print(result)