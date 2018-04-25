from python.Edge import Edge
from python.Node import Node
from python.util import get_t_distance_preserving_edges

t = 1.2

path = [
    Node('a', 0, 9),
    Node('b', 3, 9),
    Node('c', 4, 10),
    Node('d', 9, 5),
    Node('e', 11, 1),
    Node('f', 16, 4),
    Node('g', 21, 5),
    Node('h', 21, 6),
    Node('i', 26, 9),
    Node('j', 27, 3)
]

# path = [Edge(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

edges = get_t_distance_preserving_edges(path, t)

for e in edges:
    print(e)
