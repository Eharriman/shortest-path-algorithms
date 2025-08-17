import sys
from typing import Tuple
from src.core.graph import Graph

class NegativeWeightCycleError(Exception):
    def __init__(self, cycle):
        self.cycle = cycle
        super().__init__(f"Graph contains negative-weight cycle: {cycle}")

def bellman_ford(graph: Graph, src: str) -> Tuple[dict, dict]:
    # distance/prev ptr. dictionaries
    dist = {node: float('inf') for node in graph.nodes}
    prev = {node: None for node in graph.nodes}

    # Queue for unvisited nodes
    #Q = set(graph.nodes)

    # initial conditions for source node
    dist[src] = 0

    for _ in range(len(graph.nodes) - 1):
        for u in graph.nodes:
            for v, weight in graph.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u

    for u in graph.nodes:
        for v, weight in graph.adj[u]:
            if dist[u] + weight < dist[v]:

                visited = {node: False for node in graph.nodes}
                curr = v
                while not visited[curr]:
                    visited[curr] = True
                    curr = prev[curr]

                cycle = [curr]
                walk = prev[curr]
                while walk != curr:
                    cycle.insert(0, walk)
                    walk = prev[walk]
                raise NegativeWeightCycleError(cycle)

    return dist, prev