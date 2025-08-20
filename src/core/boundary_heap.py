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

    def pull(self):
        """
        To retrieve the smallest M values from D0 ∪ D1, we collect a sufficient prefix of blocks from D0
        and D1 separately, denoted as S′
        0 and S′
        1, respectively. That is, in D0 (D1) we start from the first block
        and stop collecting as long as we have collected all the remaining elements or the number of collected
        elements in S′
        0 (S′
        1) has reached M . If S′
        0 ∪ S′
        1 contains no more than M elements, it must contain all
        blocks in D0 ∪ D1, so we return all elements in S′
        0 ∪ S′
        1 as S′ and set x to the upper bound B, and the
        time needed is O(|S′|). Otherwise, we want to make |S′| = M , and because the block sizes are kept
        at most M , the collecting process takes O(M ) time.
        Now we know the smallest M elements must be contained in S′
        0 ∪S′
        1 and can be identified from S′
        0 ∪S′
        1
        as S′ in O(M ) time. Then we delete elements in S′ from D0 and D1, whose running time is amortized
        to insertion time. Also set returned value x to the smallest remaining value in D0 ∪ D1, which can also
        be found in O(M ) time
        :return:
        """

        Si = set()
        Bi = None

        if not self.heap:
            return float('inf'), set()
