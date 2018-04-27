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

    def __repr__(self, level=0):
        result = ""
        name = self.name
        if self.left is not None:
            result += self.right.__repr__(level + 1) + "\n"

        if isinstance(self.name, (float, int)):
            name = int(self.name)

        result += "\t" * level + repr(name)
        if self.right is not None:
            result += "\n" + self.left.__repr__(level + 1)

        return result
