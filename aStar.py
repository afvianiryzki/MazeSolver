import PriorityQueue as pq
import Element as el
import Matrix as M
import main as m
import turtle


class aStar(object):
    def __init__(self):
        self.opened = pq.PriorityQueue()
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
        g = current.gx + 10
        nextTo.setGx(g)
        h = self.getHx(nextTo)
        nextTo.setHx(h)
        f = g + h
        nextTo.setFx(f)
        nextTo.setParent(current)
        self.opened.insert(nextTo)

    def walkTo(self, current):
        s.goto(-400 + (current.y * 24), 400 - (current.x*24))
        s.stamp()
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

    def getPath(self):
        p.goto(-400 + (self.mazeEnd.y * 24), 400 - (self.mazeEnd.x*24))
        p.stamp()
        akhir = self.mazeEnd
        path = [[akhir.x, akhir.y]]
        while (akhir is not self.mazeStart):
            self.maze.matrix[akhir.x][akhir.y] = 4
            p.goto(-400 + (akhir.y * 24), 400 - (akhir.x*24))
            p.stamp()
            akhir = akhir.parent
            path.append([akhir.x, akhir.y])
        path.append([self.mazeStart.x, self.mazeStart.y])
        self.maze.matrix[akhir.x][akhir.y] = 4
        p.goto(-400 + (akhir.y * 24), 400 - (akhir.x*24))
        p.stamp()

        
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


maze = m.main()
global w
w = m.wall()
global f
f = m.floor()
global s 
s = m.search()
global p
p = m.path()

global wn

wn = turtle.Screen()
wn.bgcolor("black")
wn.screensize(1000,1000) 
wn.title("A STAR MAZE SOLVER")
for y in range(maze.row):
    for x in range(maze.col):
        character = maze.matrix[y][x]
        screen_x = -400 + (x * 24)
        screen_y = 400 - (y * 24)

        if character == 1:
            w.goto(screen_x, screen_y)
            w.stamp()
        elif character == 0:
            f.goto(screen_x, screen_y)
            f.stamp()

astar = aStar()
astar.createMaze(maze)
astar.letsgo()

wn.mainloop()