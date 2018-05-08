from python.Nodes import PathNode
import python.split_tree as SplitTree
import python.wspd as WSPD
import python.util as util
import matplotlib.pyplot as plt

import python.plots as plots

t = 1.2
epsilon = 0.05
s = (12 + 24 * (1 + epsilon / 3) * t) / epsilon
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
    PathNode('l', 55, 16),
    PathNode('m', 100, 20)
]
n = len(path)


def plot_shortest_path(path, indices):
    x_list = [path[i].x for i in indices]
    y_list = [path[i].y for i in indices]
    line = plt.plot(x_list, y_list)
    plt.setp(line, color='lightgreen', linewidth=2)


def print_edges(edges):
    for e in edges:
        print(e)


def print_edge_lengths(path, S):
    for i in range(len(path) - 1):
        print("Edge between " + path[i].name + " and " + path[i + 1].name + ":\t" + str(S[i + 1] - S[i]))


def plot_edge_lengths():
    plots.plot_points(path, [0, 4], 'red')
    plots.plot_text_on_edge(path[0], path[1], round(S[1], 1), (-1.5, -1.5))
    plots.plot_text_on_edge(path[1], path[2], round(S[2] - S[1], 1), (0.15, -1))
    plots.plot_text_on_edge(path[2], path[3], round(S[3] - S[2], 1), (0, -1.5))
    plots.plot_text_on_edge(path[3], path[4], round(S[4] - S[3], 1), (0.8, -0.3))
    plots.plot_text_on_edge(path[0], path[4], round(util.euclidean_distance(path[0], path[4]), 1), (-1, 1))


S = util.flatten_path(path)
edges = util.get_t_distance_preserving_edges(path, t, S)
# edges_epsilon = util.get_t_epsilon_distance_preserving_edges(path, t, epsilon, S)

# print_edge_lengths(path, S)
# print("Euclidean:\t" + str(util.euclidean_distance(path[0], path[4])))
# print("Euclidean*t:\t" + str(util.euclidean_distance(path[2], path[4])*1.1))
# print("delta: \t" + str((S[4]-S[2])))

plots.plot_path(path)

# plots.plot_edges(edges_epsilon, 'green')
# plots.plot_edges(edges, 'orange')
plot_shortest_path(path, [0, 2, 4, 6, 7, 8, 9, 11, 12])


plt.show()

T = SplitTree.compute_split_tree(S, 0, n - 1)
# print(T.to_string())
# WSPD.compute_wspd(T, S, s)
