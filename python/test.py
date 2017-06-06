from gturtle import*
from gpanel import*
from random import*

XMAX = 800
YMAX = 400

tf = TurtleFrame()

landmine = Turtle(tf)
landmine.hideTurtle()

robot = Turtle(tf)
robot.setColor("black")
robot.setPenColor("blue")
robot.setPos(0, -200)

# Draw frame
landmine.setPenColor("black")
landmine.penDown()
landmine.setPos(-400,-200)
landmine.forward(400)
landmine.right(90)

# Place mines
landmine.setPenColor("red")
landmine.setPos(0, 0)
landmine.penUp()
repeat 500:
    landmine.setPos(randint(-XMAX/2,XMAX/2), randint(-YMAX/2,YMAX/2))
    landmine.penDown()
    landmine.dot(5)
    landmine.penUp()

#makeTurtle()
#hideTurtle()
##repeat 4:
#    forward(25)
#    left(90)

# Generate minefield
#setColor("red")

#for x in range(0, 250):
#    move(randint(-49,49),randint(-49,49))
#    fillRectangle(2,2)





