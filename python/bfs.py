

def create_adjacency_list(path, edges):
    result = {}
    for node in path:
        result[node.name] = []
    for edge in edges:
        result[edge.tail.name].append(edge.head.name)
    return result


def shortest_path(adjacency_list, start_index, target_index):
    d = (len(adjacency_list.keys())+1) * [-1]
    d[start_index] = 0
    p = (len(adjacency_list.keys())+1) * [None]
    queue = [start_index]
    current = None
    while len(queue) != 0 and current != target_index:
        current = queue.pop()
        for node in adjacency_list[current]:
            if d[node] < 0:
                queue.append(node)
                d[node] = d[current] + 1
                p[node] = current

    shortest_path = [current]
    while p[current] is not None:
        current = p[current]
        shortest_path.append(current)

    return list(reversed(shortest_path))
