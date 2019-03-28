import colorama
from colorama import Fore, Back, Style

class Matrix(object):
    def __init__(self, number):
        self.matrix = []
        for line in number:
            self.el = []
            for element in line:
                self.el.append(int(element))
            self.matrix.append(self.el)
        
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])

        print("Enter your start point: ")
        sPoint = input().split(" ")
        self.start = [int(num) for num in sPoint]

        print("Enter your end point: ")
        ePoint = input().split(" ")
        self.end = [int(num) for num in ePoint]

    def setEl(self, i, j, val):
        self.matrix[i][j] = val
    
    def getEl(self, i, j):
        return self.matrix[i][j]

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getObstacle(self):
        self.obstacle = []
        for i in range(self.row):
            for j in range(self.col):
                if (self.matrix[i][j] == 1):
                    self.obstacle.append([i,j])
        return self.obstacle

    def getAvailable(self):
        self.available = []
        for i in range(self.row):
            for j in range(self.col):
                if (self.matrix[i][j] == 0):
                    self.available.append([i,j])
        return self.available
    
    def print(self):
        colorama.init()
        print(Fore.CYAN)
        for x in self.matrix:
            for y in x:
                if(y == 0):
                    print(" ", end="")
                elif(y== 1):
                    print("▓", end="")
                elif(y == 3):
                    print("x", end="")
                elif(y == 4):
                    print("o", end="")
            print()
        print(Fore.RESET)
        print(Fore.GREEN, "Your start point : ", self.getStart())
        print(Fore.RED, "Your end point   : ", self.getEnd(), Fore.RESET)