import sys
import Matrix as M
import colorama
from colorama import Fore, Back, Style

def main():
    infile = open(sys.argv[1]).read()
    number = [item for item in infile.split('\n')]
    
    maze = M.Matrix(number)
    maze.print()
    

main()
