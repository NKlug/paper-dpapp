import matplotlib.pyplot as plt


def plot_path(path):
    plt.figure(figsize=(30, 20))
    x_list = [node.x for node in path]
    y_list = [node.y for node in path]
    lines = plt.plot(x_list, y_list)
    plt.setp(lines, linewidth=2, color='black')
    plt.grid(True)


def plot_edges(edges, color):
    for edge in edges:
        line = plt.plot([edge.head.x, edge.tail.x], [edge.head.y, edge.tail.y])
        plt.setp(line, color=color)