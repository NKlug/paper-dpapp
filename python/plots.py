import matplotlib.pyplot as plt


def plot_path(path):
    plt.figure(figsize=(30, 20))
    x_list = [node.x for node in path]
    y_list = [node.y for node in path]
    lines = plt.plot(x_list, y_list)
    plt.setp(lines, linewidth=3, color='black')
    plt.grid(True)


def plot_edges(edges, color):
    for edge in edges:
        line = plt.plot([edge.head.x, edge.tail.x], [edge.head.y, edge.tail.y])
        plt.setp(line, linewidth=2,  color=color)


def plot_points(path, indices, color):
    x_list = [path[i].x for i in indices]
    y_list = [path[i].y for i in indices]
    lines = plt.plot(x_list, y_list)
    plt.setp(lines, linewidth=2, color=color)

