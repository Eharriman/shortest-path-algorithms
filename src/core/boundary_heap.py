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
        pass