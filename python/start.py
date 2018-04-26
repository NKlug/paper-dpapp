from python.Node import Node
from python.util import get_t_distance_preserving_edges
import matplotlib.pyplot as plt

t = 1.2

path = [
    Node('a', 0, 15),
    Node('b', 4, 12),
    Node('c', 8, 13),
    Node('d', 16, 12),
    Node('e', 25, 24),
    Node('f', 27, 19),
    Node('g', 24, 13),
    Node('h', 34, 13),
    Node('i', 38, 0),
    Node('j', 51, 2),
    Node('k', 54, 16),
    Node('l', 55, 16)
]


def plot_path(path):
    plt.figure(figsize=(30, 20))
    x_list = [node.x for node in path]
    y_list = [node.y for node in path]
    # plt.gca().set_color_cycle(['black'])
    lines = plt.plot(x_list, y_list)
    plt.setp(lines, linewidth=2, color='black')
    plt.axis([0, 60, 0, 25])
    plt.grid(True)


def plot_t_distance_preserving(path):
    edges = get_t_distance_preserving_edges(path, t)
    for edge in edges:
        line = plt.plot([edge.head.x, edge.tail.x], [edge.head.y, edge.tail.y])
        plt.setp(line, color='orange')


def plot_shortest_path(path):
    x_list = [path[0].x, path[2].x, path[4].x, path[6].x, path[7].x, path[8].x, path[9].x, path[11].x]
    y_list = [path[0].y, path[2].y, path[4].y, path[6].y, path[7].y, path[8].y, path[9].y, path[11].y]
    line = plt.plot(x_list, y_list)
    plt.setp(line, color='red', linewidth=3)


# path = [Edge(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

edges = get_t_distance_preserving_edges(path, t)

for e in edges:
    print(e)

plot_path(path)
plot_t_distance_preserving(path)
plot_shortest_path(path)
plt.show()
