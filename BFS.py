import RegularQueue as rq
import Element as el
import Matrix as M


class BFS(object):
    def __init__(self):
        self.opened = rq.RegularQueue()
        self.closed = set()

        self.element = []

    def getElement(self, x, y):
        return self.element[x][y]

    def createMaze(self, matrix):
        self.maze = matrix
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


    def getPath(self):
        akhir = self.mazeEnd
        path = [[akhir.x, akhir.y]]
        while (akhir is not self.mazeStart):
            self.maze.matrix[akhir.x][akhir.y] = 4
            akhir = akhir.parent
            path.append([akhir.x, akhir.y])
        path.append([self.mazeStart.x, self.mazeStart.y])
        self.maze.matrix[akhir.x][akhir.y] = 4

        
    def letsgo(self):
        current = self.mazeStart
        self.maze.matrix[current.x][current.y] = 3
        self.closed.add(self.mazeStart)
        self.walkTo(current)
        if (current.x == self.mazeEnd.x and current.y == self.mazeEnd.y):
                return self.getPath()
        
        while(len(self.opened.queue)):
            self.closed.add(current)
            current = self.opened.delete()
            self.maze.matrix[current.x][current.y] = 3
            self.walkTo(current)
            if (current.x == self.mazeEnd.x and current.y == self.mazeEnd.y):
                return self.getPath()