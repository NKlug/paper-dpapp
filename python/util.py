from scipy.spatial import distance
from python.Edge import Edge


def get_t_distance_preserving_edges(path, t, distances):
    result = []
    for i in range(len(path)):
        for j in range(i + 2, len(path)):
            if is_t_distance_preserving(path, i, j, t, distances):
                result.append(Edge(path[i], path[j]))

    return result


def get_t_epsilon_distance_preserving_edges(path, t, epsilon, distances):
    result = []
    for i in range(len(path)):
        for j in range(i + 2, len(path)):
            if is_t_epsilon_distance_preserving(path, i, j, t, epsilon, distances):
                result.append(Edge(path[i], path[j]))

    return result


def is_t_distance_preserving(path, i, j, t, distances):
    return delta(i, j, distances) <= t * euclidean_distance(path[i], path[j])


def is_t_epsilon_distance_preserving(path, i, j, t, epsilon, distances):
    return delta(i, j, distances) <= (1 + epsilon) * t * euclidean_distance(path[i], path[j])


def euclidean_distance(node1, node2):
    return distance.euclidean([node1.x, node1.y], [node2.x, node2.y])


def delta(i, j, distances):
    return distances[j] - distances[i]


def flatten_path(path):
    result = [0]
    current_distance = 0
    for i in range(len(path) - 1):
        current_distance += euclidean_distance(path[i], path[i + 1])
        result.append(current_distance)
    return result


def get_all_dilations(path, S):
    result = [1]
    for i in range(len(path)):
        for j in range(i + 2, len(path)):
            result.append(delta(i, j, S) / euclidean_distance(path[i], path[j]))
    return sorted(result)
