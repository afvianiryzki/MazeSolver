import sys
import readMatrix as mat
import colorama
from colorama import Fore, Back, Style

def main():
    maze = mat.generateMatrix(sys.argv[1])
    row = len(maze)
    col = len(maze[0])
    
    colorama.init()
    print(Fore.YELLOW)
    print()

    for x in maze:
        print(*x, sep="")

    print(Style.RESET_ALL)

    point = mat.searchStartEnd(maze, row, col)

    print(Fore.GREEN)
    print("Start point   : ", point[0])
    print(Fore.RED + "End point     : ", point[1])
    print(Fore.RESET)
    print()

main()