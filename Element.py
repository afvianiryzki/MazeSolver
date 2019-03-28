class Element(object):
    def __init__(self, x, y, available):
        self.x = x
        self.y = y
        self.available = available
        self.parent = None

        self.fx = 0
        self.gx = 0
        self.hx = 0

    def getPos(self):
        return self.x, self.y

    def setFx(self, fx):
        self.fx = self.gx + self.hx
    
    def setGx(self, gx):
        self.gx = gx
    
    def setHx (self, hx):
        self.hx = hx
    
    def setParent(self, parent):
        self.parent = parent






























































        