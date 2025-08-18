from src.core.graph import Graph
from src.core.bellman_ford import bellman_ford

graph1 = Graph(directed=True)

graph1.add_edge('A', 'B', 4)
graph1.add_edge('A', 'C', 8)
graph1.add_edge('B', 'E', 6)
graph1.add_edge('C', 'D', 2)
graph1.add_edge('D', 'E', 10)

result = bellman_ford(graph1, 'A')

print(result)