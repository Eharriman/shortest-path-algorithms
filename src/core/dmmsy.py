from src.core.graph import Graph
import heapq

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

    def base_case(self, B, S):
        """

        :param B:
        :param S:
        :return:
        """

        assert len(S) == 1
        x = next(iter(S))

        U0 = {x}
        # Binary heap w/ singleton element and distance. See Algorithm 2 line 3.
        heap = [(self.bd[x], x)]

        visited = set()

        while heap and len(U0) < self.k + 1:
            d_u, u = heapq.heappop(heap) # Line 5. Extract the minimum

            if u in visited:
                continue
            visited.add(u)
            U0.add(u)

            for v, w_uv in self.graph.get_neighbours(u):
                new_dist = self.bd[u] + w_uv
                if new_dist < self.bd[v] and new_dist < B:
                    self.bd[v] = new_dist
                    heapq.heappush(heap, (self.bd[v], v))

        if len(U0) <= self.k:
            return B, U0
        else:
            B_prime = max(self.bd[v] for v in U0)
            U = {v for v in U0 if self.bd[v] < B_prime}
            return B_prime, U