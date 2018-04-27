from python.Nodes import PathNode
import python.split_tree as SplitTree
import python.wspd as WSPD
import python.util as util
import matplotlib.pyplot as plt

t = 1.2
epsilon = 0.05
s = (12 + 24 * (1 + epsilon/3) * t) / epsilon
path = [
    PathNode('a', 0, 15),
    PathNode('b', 4, 12),
    PathNode('c', 8, 13),
    PathNode('d', 16, 12),
    PathNode('e', 25, 24),
    PathNode('f', 27, 19),
    PathNode('g', 24, 13),
    PathNode('h', 34, 13),
    PathNode('i', 38, 0),
    PathNode('j', 51, 2),
    PathNode('k', 54, 16),
    PathNode('l', 55, 16)
]
n = len(path)


def plot_path(path):
    plt.figure(figsize=(30, 20))
    x_list = [node.x for node in path]
    y_list = [node.y for node in path]
    # plt.gca().set_color_cycle(['black'])
    lines = plt.plot(x_list, y_list)
    plt.setp(lines, linewidth=2, color='black')
    plt.axis([0, 60, 0, 25])
    plt.grid(True)


def plot_edges(edges, color):
    for edge in edges:
        line = plt.plot([edge.head.x, edge.tail.x], [edge.head.y, edge.tail.y])
        plt.setp(line, color=color)


def plot_shortest_path(path):
    x_list = [path[0].x, path[2].x, path[4].x, path[6].x, path[7].x, path[8].x, path[9].x, path[11].x]
    y_list = [path[0].y, path[2].y, path[4].y, path[6].y, path[7].y, path[8].y, path[9].y, path[11].y]
    line = plt.plot(x_list, y_list)
    plt.setp(line, color='red', linewidth=3)


def print_edges(edges):
    for e in edges:
        print(e)


# path = [Edge(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

edges = util.get_t_distance_preserving_edges(path, t)
edges_epsilon = util.get_t_epsilon_distance_preserving_edges(path, t, epsilon)
S = util.flatten_path(path)

plot_path(path)
plot_edges(edges_epsilon, 'green')
plot_edges(edges, 'orange')
# plot_shortest_path(path)
# plt.show()

print(S)
T = SplitTree.compute_split_tree(S, 0, n-1)
WSPD.compute_wspd(T, S, s)


