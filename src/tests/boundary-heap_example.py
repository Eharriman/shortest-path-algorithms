from src.core.boundary_heap import BoundaryHeap

def test_initialize():
    print("++++ Testing the initialization method ++++")
    bheap = BoundaryHeap()
    bheap.initialize(M=4, B=100)
    assert bheap.bound == 100
    print("Passed.")

def test_insert_pull():
    print("++++ Testing the insert/pull method ++++")
    bheap = BoundaryHeap()
    bheap.insert('A', 5)
    bheap.insert('A', 5)
    bheap.insert('B', 3)
    bheap.insert('C', 3)
    bheap.insert('D', 7)

    B1, S1 = bheap.pull()

    assert B1 == 3
    assert S1 == {'B', 'C'}

    print("Passed.")

def test_batch_prepend():
    print("++++ Testing the batch-prepend method ++++")
    bheap = BoundaryHeap()
    bheap.insert('A', 10)
    batch = [('B', 5), ('C', 5)]
    bheap.batch_prepend(batch)

    B, S = bheap.pull()
    assert B == 5
    assert S == {'B', 'C'}
    print("Passed.")


test_initialize()
test_insert_pull()
test_batch_prepend()
