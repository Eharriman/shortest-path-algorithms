from src.core.graph import Graph
from src.core.boundary_heap import BoundaryHeap
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

    def _get_weight(self, u, v):
        for neighbour, weight in self.graph.get_neighbours(u):
            if neighbour == v:
                return weight
        return float('inf')

    def _find_roots(self, forest, v):
        while v in forest:
            v = forest[v]
        return v

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

    def bmssp(self, lvl, B, S):
        """

        :param lvl: Recursion level. Called l in the paper.
        :param B:
        :param S:
        :return:
        """
        M = 2 ** ((lvl - 1) * self.t)

        # lvl == 0 is the base case for bmssp. Call w/  B and S.
        if lvl == 0:
            return self.base_case(B, S)

        # Step 4
        P, W = self.find_pivots(B, S)

        # Step 5-6.
        D = BoundaryHeap()
        D.initialize(M, B)

        # Initialize D with elements from P:
        for x in P:
            D.insert(x, self.bd[x])

        U = set()
        if P:
           B_prime_0 = min(self.bd[x] for x in P)
        else:
            B_prime_0 = B

        i = 0
        B_prime = B_prime_0

        while len(U) < self.k * 2 ** (lvl * self.t) and not D.is_empty():
            i += 1


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

    def find_pivots(self, B, S):
        W = set(S)
        Wi_prev = set(S)

        forest_parents = dict()

        for _ in range(self.k):
            Wi = set()

            # Ho to ensure u ∈ Wi−1
            for u in Wi_prev:
                for v, w_uv in self.graph.get_neighbours(u):
                    new_dist = self.bd[u] + w_uv

                    if new_dist < self.bd[v]:
                        # Wi <- Wi ∪ {v}. Add v to the set?
                        self.bd[v] = new_dist
                        Wi.add(v)
                        forest_parents[v] = u
                        #W ← W ∪ Wi

            if not Wi:
                break

            W.update(Wi)
            Wi_prev = Wi

            if len(W) > self.k * len(S):
                return set(S), W

            # Build forest F: all (u,v) ∈ E with u,v ∈ W and bd[v] = bd[u] + w_uv
            forest = {v: u for v, u in forest_parents.items() if v in W and u in W and self.bd[v] == self.bd[u] + self._get_weight(u, v)}

            # Count size of trees rooted at each s ∈ S
            subtree_sizes = {s: 0 for s in S}

            for v in forest:
                root = self._find_roots(forest, v)
                if root in subtree_sizes:
                    subtree_sizes[root] += 1

            # Select pivots
            P = {s for s, size in subtree_sizes.items() if size >= self.k}

            return P, W


