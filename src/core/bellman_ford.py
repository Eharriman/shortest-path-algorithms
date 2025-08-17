import sys
from typing import Tuple
from src.core.graph import Graph

def bellman_ford(graph: Graph, src: str) -> Tuple[dict, dict]:
    # distance/prev ptr. dictionaries
    dist = {node: float('inf') for node in graph.nodes}
    prev = {node: None for node in graph.nodes}

    # Queue for unvisited nodes
    Q = set(graph.nodes)

    # initial conditions for source node
    dist[src] = 0


    return dist, prev