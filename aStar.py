import heapq

class Cell(object):
    def __init__(self, x, y, wall):
        self.x = x
        self.y = y
        self.wall = wall

        self.parent = None

        self.fx = 0 # f(x) = g(x) + h(x)
        self.gx = 0 # cost from start position to current position 
        self.hx = 0 # cost from current position to end postion (manhattan distance)

class aStar(object):
    def __init__(self, maze):
        self.opened = []