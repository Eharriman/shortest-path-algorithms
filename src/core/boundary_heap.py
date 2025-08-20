import heapq

class BoundaryHeap:
    """
    This class is an implementation of the data structure defined in Lemma 3.3. (pg. 6-7)
    """
    def __init__(self):
        self.heap = []
        self.entry_map = {}
        self.counter = 0
        self.deleted = set()
        self.bound = float('inf')

    def initialize(self, M, B):
        """
        :param M: This is an integer parameter
        :param B: This is the upper bound on all involved values
        :return:
        """
        self.heap = []
        self.entry_map = {}
        self.counter = 0
        self.bound = B
        self.deleted.clear()
        #pass

    def insert(self, node, value):
        """
        Key pair <a,b>: check if a is in heap, and if so repalce if b < b'.
        <a,b> then placed in D1 depending on the bound?
        :param node:
        :param value:
        :return:
        """
        if node in self.entry_map:
            old_val, _ = self.entry_map[node]
            if value >= old_val:
                return
            self.deleted.add((old_val, node))

        entry = (value, self.counter, node)
        self.entry_map[node] = (value, self.counter)
        heapq.heappush(self.heap, entry)
        self.counter += 1