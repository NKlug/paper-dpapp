from scipy.spatial import distance

class Edge(object):

    def __init__(self, tail, head):
        self.tail = tail
        self.head = head
        self.length = self.euclidean_distance()

    def euclidean_distance(self):
        return distance.euclidean([self.tail.x, self.tail.y], [self.head.x, self.head.y])

    def __str__(self):
        return "(" + str(self.tail.name) + ", " + str(self.head.name) + ")"
