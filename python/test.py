from gturtle import*
from gpanel import*
from random import randint

width = 800
height = 400
delta = 40 # Max robot speed

# Define list variables to keep track of landmines
xmines = list()
ymines = list()

tf = TurtleFrame()

# Set up mine turtle
landmine = Turtle(tf)
landmine.hideTurtle()

# Draw frame
landmine.setPenColor("black")
landmine.penDown()
landmine.setPos(-402,-202)
repeat 2:
    landmine.forward(height+4)
    landmine.right(90)
    landmine.forward(width+4)
    landmine.right(90)

# Generate coordinates of mines
for i in range(250):
    x = randint(-width/2, width/2)
    y = randint(-height/2, height/2)
    xmines.append(x)
    ymines.append(y)

# Place mines
landmine.setPenColor("red")
landmine.setPos(0, 0)
landmine.penUp()
for i in range(250):
    landmine.setPos(xmines[i], ymines[i])
    landmine.penDown()
    landmine.dot(5)
    landmine.penUp()

# Set up robot
robot = Turtle(tf)
robot.setColor("black")
robot.setPenColor("blue")
robot.setPos(-width/2, -height/2)

t = 60
direction = 1 # 1 = up, -1 = down
switchDirection = False
while t >= 0:
    print t
    
    y= robot.getY()
    if y >= height/2:
        direction = -1
        robot.right(90)
        robot.forward(20)
        robot.left(90)
    if y <= -height/2:
        direction = 1
        robot.right(90)
        robot.forward(20)
        robot.left(90)


    robot.forward(delta * direction)

    t -= 1




