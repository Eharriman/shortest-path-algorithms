from src.core.graph import Graph

class DMMSY:
    def __init__(self, graph, k, t):
        """
        Initialization for DMMSY class
        :param graph: Graph data structure defined in graph.py
        :param k: k = [log^1/3(n)] parameter defined on pg. 4. This is the branching factor for D&C
        :param t: t = [log^2/3(n)] parameter defined on pg. 4. This is the depth control for D&C
        """
        self.graph = graph
        self.k = k
        self.t = t
        self.n = len(graph)

        self.bd = {v: float('inf') for v in graph}

        self.complete = set()

    def run(self, src):
        self.bd[src] = 0
        self.complete.add(src)
        # Lemma 3.1. Integer level which is bounded l ∈ [0, ⌈log(n)/t⌉]. See pg. 4
        lvl = int(self.n.bit_length() // self.t)

        # The Bound as defined pg. 5 is initialized at B = infinity
        B = float('inf')
        # The set of vertices, S, includes the source vertex
        S = {src}

        pass
