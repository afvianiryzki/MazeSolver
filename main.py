import sys
import Matrix as M
import aStar as A
import BFS as B
import colorama
from colorama import Fore, Back, Style


def main():
    infile = open(sys.argv[1]).read()
    number = [item for item in infile.split('\n')]
    
    mazeAS = M.Matrix(number)
    mazeBFS = M.Matrix(number)
    #maze.print()

    li = [1,2,3,4,5]
    del li[0]
    print(li[0])
    

    astar = A.aStar()
    astar.createMaze(mazeAS)
    astar.letsgo()
    mazeAS.print()

    bfs = B.BFS()
    bfs.createMaze(mazeBFS)
    bfs.letsgo()
    mazeBFS.print()


main()
