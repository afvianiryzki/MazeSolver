import turtle
import Matrix as M
import sys

wn = turtle.Screen()
wn.bgcolor = ("light grey")
wn.title = ("A MAZE GAME - ASTAR")
wn.setup(700,700)

class wall(turtle.Turtle):
    def __init___(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class floor(turtle.Turtle):
    def __init___(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("light grey")
        self.penup()
        self.speed(0)

def buildMaze(maze):
    for y in range(maze.row):
        for x in range(maze.col):
            posx = -288 + (x*24)
            posy = 288 - (y*24)
            if(maze.matrix[y][x] == 0):
                f.goto(posx,posy)
                f.stamp()
            elif(maze.matrix[y][x] == 1):
                w.goto(posx, posy)
                w.stamp()

infile = open(sys.argv[1]).read()
number = [item for item in infile.split('\n')]

mazeAS = M.Matrix(number)
w = wall()
f = floor()
buildMaze(mazeAS)

while true:
    pass
