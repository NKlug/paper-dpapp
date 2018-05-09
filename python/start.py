from python.Nodes import PathNode
import python.split_tree as SplitTree
import python.wspd as WSPD
import python.bfs as bfs
import python.util as util
import matplotlib.pyplot as plt
import numpy as np

import python.plots as plots

t = 1.2
epsilon = 0.05
s = (12 + 24 * (1 + epsilon / 3) * t) / epsilon
path = [
    PathNode(1, 0, 15),
    PathNode(2, 4, 12),
    PathNode(3, 8, 13),
    PathNode(4, 16, 12),
    PathNode(5, 25, 24),
    PathNode(6, 27, 19),
    PathNode(7, 24, 13),
    PathNode(8, 34, 13),
    PathNode(9, 38, 0),
    PathNode(10, 51, 2),
    PathNode(11, 54, 16),
    PathNode(12, 55, 16),
    PathNode(13, 100, 20)
]
n = len(path)


def plot_approximation(path, indices):
    x_list = [path[i].x for i in indices]
    y_list = [path[i].y for i in indices]
    line = plt.plot(x_list, y_list)
    plt.setp(line, color='green', linewidth=5)


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
t_edges = util.get_t_distance_preserving_edges(path, t, S)
all_edges = util.get_path_edges(path) + t_edges

adjacency_list = bfs.create_adjacency_list(path, all_edges)
# edges_epsilon = util.get_t_epsilon_distance_preserving_edges(path, t, epsilon, S)

# print_edge_lengths(path, S)
# print("Euclidean:\t" + str(util.euclidean_distance(path[0], path[4])))
# print("Euclidean*t:\t" + str(util.euclidean_distance(path[2], path[4])*1.1))
# print("delta: \t" + str((S[4]-S[2])))

shortest_path = bfs.shortest_path(adjacency_list, 1, n)
plots.plot_path(path, 5)
# plots.plot_edges(edges_epsilon, 'green')
plots.plot_edges(t_edges, 'orange')
plot_approximation(path, np.array(shortest_path) - 1)
plt.show()

T = SplitTree.compute_split_tree(S, 0, n - 1)
# print(T.to_string())
# WSPD.compute_wspd(T, S, s)
