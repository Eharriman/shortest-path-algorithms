from src.core.boundary_heap import BoundaryHeap

def test_initialize():
    print("++++ Testing the initialization method ++++")
    bheap = BoundaryHeap()
    bheap.initialize(M=4, B=100)
    assert bheap.bound == 100
    print("Passed.")


test_initialize()
    