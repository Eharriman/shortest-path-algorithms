import sys
from typing import Tuple
from graph import Graph


def dijkstra(graph: graph.Graph, src: str) -> Tuple[dict, dict]:

    # Distance and ptr. dictionaries
    dist = {}
    prev = {}

    # Priority  queue
    Q = set()

    for n in graph.nodes:
        # set dist[n]
        dist[n] = [sys.maxsize]
        prev[n] = None
        Q.add(n)
        #prev[n]

    dist[src] = 0

    #while Q not

    return dist, prev