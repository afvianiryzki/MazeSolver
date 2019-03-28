import PriorityQueue as pq
import Element as el
import Matrix as M

class aStar(object):
    def __init__(self):
        self.opened = pq.PriorityQueue()
        self.closed = set()

        self.element = []
        self.mazeRow = None
        self.mazeCol = None

    def getElement(self, x, y):
        return self.element[x][y]

    def createMaze(self, matrix):
        self.mazeRow = matrix.row
        self.mazeCol = matrix.col
        
        for i in range(self.mazeRow):
            elementLine = []
            for j in range(self.mazeCol):
                if ([i,j]) in matrix.getAvailable():
                    available = True
                else:
                    available = False
                elementLine.append(el.Element(i,j, available))
            self.element.append(elementLine)
        
        self.mazeStart = self.getElement(*matrix.getStart())
        self.mazeEnd = self.getElement(*matrix.getEnd())
    
    def updateElmt(self, current, nextTo):
        g = current.gx + 10
        nextTo.setGx(g)
        h = self.getHx(nextTo)
        nextTo.setHx(h)
        f = g + h
        nextTo.setFx(f)
        nextTo.setParent(current)
        self.opened.insert(nextTo)

    def walkTo(self, current):
        xn = current.x
        xm = current.x-1
        xp = current.x+1
        yn = current.y
        ym = current.y-1
        yp = current.y+1

        if(yp < self.mazeCol):
            if(self.element[xn][yp].available and self.element[xn][yp] not in self.closed):
                self.updateElmt(current, self.element[xn][yp])
        
        if(xp < self.mazeRow):
            if(self.element[xp][yn].available and self.element[xp][yn] not in self.closed):
                self.updateElmt(current, self.element[xp][yn])
        
        if(ym >= 0):
            if(self.element[xn][ym].available and self.element[xn][ym] not in self.closed):
                self.updateElmt(current, self.element[xn][ym])

        if(xm >= 0):
            if(self.element[xm][yn].available and self.element[xm][yn] not in self.closed):
                self.updateElmt(current, self.element[xm][yn])


    def getHx(self, elmt):
        return (10*(abs(self.mazeEnd.x - elmt.x) + abs(self.mazeEnd.y - elmt.y)))

    def letsgo(self):
        current = self.mazeStart
        self.closed.add(self.mazeStart)

        self.walkTo(current)
        

        #while(len(self.opened.queue)):
        #    current = 


        """print(self.current.x)
        print(self.current.y)
        print(self.element[0][0].gx)
        print(self.current.y)"""

        """if(self.getElement(self.current.x-1, self.current.y).available):
            self.element[self.current.x-1][self.current.y].setGx(self.current.gx + 10)
            self.element[self.current.x-1][self.current.y].setHx(self.getHx())
            self.opened.insert(self.getElement)
        while (self.current is not self.mazeEnd):"""
            