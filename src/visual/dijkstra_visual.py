import sys
from typing import Tuple
from src.core.graph import Graph
from src.visual.graph_visual import GraphVisualizer


def dijkstra(graph: Graph, src: str, visualizer: GraphVisualizer) -> Tuple[dict, dict]:
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
        # Tracking visited node for visualization
        visited.add(u)

        highlight_nodes = visited.copy()
        highlight_edges = set()

        # Update length based on neighbour distance
        for neighbour, weight in graph.adj[u]:
            curr_length = dist[u] + weight
            if curr_length < dist[neighbour]:
                dist[neighbour] = curr_length
                prev[neighbour] = u
                highlight_edges.add((u, neighbour))

        visualizer.draw(
            highlight_nodes=highlight_nodes,
            highlight_edges=highlight_edges,
            title=f"Dijkstra visiting: {u}, distances: {dist}"
        )

    return dist, prev


