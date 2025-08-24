from src.core.graph import Graph
from src.core.dmmsy import DMMSY

def test_base_case():
    graph1 = Graph(directed=True)
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('B', 'C', 1)
    graph1.add_edge('C', 'D', 1)

    alg = DMMSY(graph1, k=1, t=1)
    alg.bd['A'] = 0

    B  = float('inf')
    S = {'A'}

    B_prime, U = alg.base_case(B, S)

    print("Returned B':", B_prime)
    print("Returned U:", U)
    print("bd map:", alg.bd)


def test_find_pivots():
    graph1 = Graph(directed=True)
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('B', 'C', 1)
    graph1.add_edge('C', 'D', 1)

    alg = DMMSY(graph1, k=1, t=1)
    alg.bd['A'] = 0

    B = float('inf')
    S = {'A'}

    P, W = alg.find_pivots(B, S)
    print("Pivots:", P)
    print("W reachable set:", W)

def test_bmssp():
    graph1 = Graph(directed=True)
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('A', 'C', 5)
    graph1.add_edge('B', 'C', 1)
    graph1.add_edge('C', 'D', 1)

    dmmsy = DMMSY(graph1, k=1, t=1)
    dmmsy.bd['A'] = 0
    dmmsy.complete.add('A')
    S = {'A'}
    B = float('inf')
    lvl = 2

    B_prime, U = dmmsy.bmssp(lvl, B, S)

    print("B':", B_prime)
    print("U:", U)
    print("bd map:", dmmsy.bd)



#print(test_base_case())
#print(test_find_pivots())
print(test_bmssp())