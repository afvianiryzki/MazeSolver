import sys
import Matrix as M
import aStar as A
import colorama
from colorama import Fore, Back, Style


def main():
    infile = open(sys.argv[1]).read()
    number = [item for item in infile.split('\n')]
    
    maze = M.Matrix(number)
    maze.print()
    

    tes = A.aStar()
    tes.createMaze(maze)
    tes.letsgo()


main()
