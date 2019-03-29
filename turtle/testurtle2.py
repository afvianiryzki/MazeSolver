import turtle
import random


t = turtle.Turtle()
t.speed(.01)
walls=[[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
floors=[[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
for x in range(1,20):
  wall=[]
  for y in range(0,20):
    num=random.randint(0,1)
    if num>1:
      num=1
    wall.append(num)
  walls.append(wall)
walls.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])

for x in range(1,20):
  floor=[]
  for y in range(0,20):
    num=random.randint(0,1)
    if num>1:
      num=1
    floor.append(num)
  floors.append(floor)
floors.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])

t.penup()
t.setx(-200)
t.sety(200)
  
for wall in range (0,len(walls)):
  for item in range(0,len(walls[wall])):
    if walls[wall][item]==0:
      t.penup()
    else:
      t.pendown()
    t.forward(20)
  t.penup()
  t.setx(-200)
  t.sety(t.ycor()-20)
  
  t.penup()
t.setx(-200)
t.sety(200)
t.rt(90) 
for floor in range (0,len(floors)):
  for item in range(0,len(floors[floor])):
    if floors[floor][item]==0:
      t.penup()
    else:
      t.pendown()
    t.forward(20)
  t.penup()
  t.setx(t.xcor()+20)
  t.sety(200)