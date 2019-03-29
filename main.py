import sys
import Matrix as M
#import aStar as A
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

class search(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("red")
    self.penup()
    self.speed(0)

class path(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("green")
    self.penup()
    self.speed(0)

def main():
    infile = open(sys.argv[1]).read()
    number = [item for item in infile.split('\n')]
    #maze = M.Matrix(number)
    mazeAS = M.Matrix(number)
    #mazeBFS = M.Matrix(number)
    return mazeAS


