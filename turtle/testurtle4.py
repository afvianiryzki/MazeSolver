# Get started with interactive Python
import turtle
import sys
import Matrix as M

#w = Tk()
wn = turtle.Screen()
wn.bgcolor("black")
wn.screensize(1000,1000)
wn.title("MAZE SOLVER")
#wn.ScrolledCanvas()

#create pen
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

#Create Level Setup Function

def setup_maze(level):
  for y in range(level.row):
    for x in range(level.col):
        character = level.matrix[y][x]
        screen_x = -400 + (x * 24)
        screen_y = 400 - (y * 24)

        if character == 1:
            w.goto(screen_x, screen_y)
            w.stamp()
        elif character == 0:
            f.goto(screen_x, screen_y)
            f.stamp()
    
        
        
w = wall()
f = floor()

infile = open(sys.argv[1]).read()
number = [item for item in infile.split('\n')]

mazeAS = M.Matrix(number)
setup_maze(mazeAS)

#Main Game Loop
while True:
    wn.update()