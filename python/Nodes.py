class PathNode(object):

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class TreeNode(object):

    def __init__(self, interval, parent=None, left=None, right=None, name='node'):
        self.parent = parent
        self.left = left
        self.right = right
        self.interval = interval
        self.name = name
        # the corresponding nodes that are A nodes - this node is the B node
        self.a_nodes = []
        # the corresponding nodes that are B nodes - this node is the A node
        self.b_nodes = []

    def to_string(self, level=0):
        result = ""
        if self.left is not None:
            result += self.right.to_string(level + 1) + "\n"

        result += "\t" * level + self.adjusted_interval()

        if self.right is not None:
            result += "\n" + self.left.to_string(level + 1)

        return result

    def print_wspd(self):
        # TODO
        pass

    def adjusted_interval(self):
        return str((self.interval[0]+1, self.interval[1] + 1))

    def __repr__(self):
        return str(self.interval)
