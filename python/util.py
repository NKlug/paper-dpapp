from scipy.spatial import distance

from python.Edge import Edge


def get_t_distance_preserving_edges(path, t):
    result = []
    for i in range(len(path)):
        for j in range(i + 2, len(path)):
            if is_t_distance_preserving(path, i, j, t):
                result.append(Edge(path[i], path[j]))

    return result


def is_t_distance_preserving(path, i, j, t):
    return delta(path, i, j) <= t * euclidean_distance(path[i], path[j])


def euclidean_distance(node1, node2):
    return distance.euclidean([node1.x, node1.y], [node2.x, node2.y])


def delta(path, i, j):
    sum = 0
    while i < j:
        sum += euclidean_distance(path[i], path[i + 1])
        i += 1
    return sum
