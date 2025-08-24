from src.core.graph import Graph
from src.core.dmmsy import DMMSY
import inspect

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

def test_dmmsy():
    graph1 = Graph(directed=True)
    """
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('B', 'C', 2)
    graph1.add_edge('A', 'C', 4)
    graph1.add_edge('C', 'D', 1)
    
    """
    """
    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'F', 5)
    graph1.add_edge('A', 'L', 8)
    graph1.add_edge('B', 'C', 7)
    graph1.add_edge('B', 'D', 8)
    graph1.add_edge('C', 'E', 11)
    graph1.add_edge('D', 'E', 4)
    graph1.add_edge('D', 'H', 3)
    graph1.add_edge('D', 'G', 6)
    graph1.add_edge('D', 'J', 2)
    graph1.add_edge('F', 'I', 12)
    graph1.add_edge('I', 'J', 9)
    graph1.add_edge('I', 'K', 2)
    """

    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'C', 3)
    graph1.add_edge('B', 'D', 5)
    graph1.add_edge('B', 'E', 3)
    graph1.add_edge('D', 'F', 1)
    graph1.add_edge('D', 'G', 7)
    graph1.add_edge('F', 'M', 6)
    graph1.add_edge('G', 'H', 4)
    graph1.add_edge('G', 'I', 3)
    graph1.add_edge('H', 'M', 2)
    graph1.add_edge('H', 'N', 5)
    graph1.add_edge('I', 'N', 1)
    graph1.add_edge('E', 'J', 4)
    graph1.add_edge('J', 'I', 2)
    graph1.add_edge('J', 'L', 2)
    graph1.add_edge('L', 'O', 3)
    graph1.add_edge('L', 'U', 5)
    graph1.add_edge('C', 'E', 6)
    graph1.add_edge('C', 'P', 2)
    graph1.add_edge('P', 'S', 3)
    graph1.add_edge('P', 'R', 9)
    graph1.add_edge('S', 'T', 6)
    graph1.add_edge('T', 'U', 3)
    graph1.add_edge('T', 'V', 7)
    graph1.add_edge('A', 'W', 6)
    graph1.add_edge('W', 'Q', 6)
    graph1.add_edge('W', 'X', 3)
    graph1.add_edge('W', 'Y', 5)
    graph1.add_edge('Q', 'R', 2)
    graph1.add_edge('X', 'Z', 2)
    graph1.add_edge('Y', 'Z', 3)
    graph1.add_edge('Z', 'V', 5)

    k = 1
    t = 1

    alg = DMMSY(graph1, k, t)
    B_prime, U = alg.run('A')

    print("Final B′:", B_prime)
    print("Set U returned:", U)
    print("bd map (shortest distances):", alg.bd)
    frame = inspect.currentframe().f_back
    linenum = frame.f_lineno
    print(f"This is from the line {linenum}")



#print(test_base_case())
#print(test_find_pivots())
#print(test_bmssp())
print(test_dmmsy())