import sys
import Matrix as M
import aStar as A
import BFS as B
import colorama
from colorama import Fore, Back, Style
import turtle



class wall(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("white")
    self.penup()
    self.speed(0)

class floor(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("black")
    self.penup()
    self.speed(0)

def setup_maze(maze, a):
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.screensize(1000,1000)
    if(a == "A"): 
        wn.title("A STAR MAZE SOLVER")
    else:
        wn.title("BFS MAZE SOLVER")
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

    while True:
        wn.update()

def main():
    infile = open(sys.argv[1]).read()
    number = [item for item in infile.split('\n')]
    #maze = M.Matrix(number)
    mazeAS = M.Matrix(number)
    #mazeBFS = M.Matrix(number)
    
    global w
    w = wall()
    global f
    f = floor()
    #global wn

    a = setup_maze(mazeAS, "A")
    #b = setup_maze(mazeBFS, "B")
 
    astar = A.aStar()
    astar.createMaze(mazeAS)
    astar.letsgo()
    #mazeAS.print()

    bfs = B.BFS()
    #bfs.createMaze(mazeBFS)
    #bfs.letsgo()
    #mazeBFS.print()

    #while True:
    #    wn.update()


main()

