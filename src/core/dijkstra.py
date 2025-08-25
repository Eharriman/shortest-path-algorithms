import sys
from typing import Tuple
from src.core.graph import Graph
from src.visual.graph_visual import GraphVisualizer


def dijkstra(graph: Graph, src: str) -> Tuple[dict, dict]:
    # distance/prev ptr. dictionaries
    dist = {node: float('inf') for node in graph.nodes}
    prev = {node: None for node in graph.nodes}

    # Queue for unvisited nodes
    Q = set(graph.nodes)

    # initial conditions for source node
    dist[src] = 0

    visited = set()

    while Q:
        # Retrieves current shortest distance for node
        u = min(Q, key=lambda n: dist[n])
        Q.remove(u)

        # Update length based on neighbour distance
        for neighbour, weight in graph.adj[u]:
            curr_length = dist[u] + weight
            if curr_length < dist[neighbour]:
                dist[neighbour] = curr_length
                prev[neighbour] = u

    return dist, prev


