# 1. Import the needed modules
import turtle
import random

# function that moves a turtle to position to draw a "starting" line
def drawLine(t, x, y, l):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(l)

# function that writes text with a turtle
def writeText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(str(text))
    
# function that will draw a race track 20 dashes long
def drawDashLine(t, x, y, dashLength, numDashes):
    t.penup()
    t.goto(x, y)
    t.pendown()
    u = 20
    #controls how many rows we'll create
    for i in range(u):
        t.penup()
        t.goto(x, y)
        #change local variable y to move down 25 px
        y = y - 25
        #before moving down again, create 10 dashes
        for j in range(numDashes):	
        	t.pendown()
        	t.forward(dashLength)
        	t.penup()
        	t.forward(dashLength)
        	t.pendown()

# function to move our turtles to the starting position
def moveTurtle(t, x, y):
	t.penup()
	t.goto(x, y)
	t.right(90)
	t.pendown()

# This function is the engine that our turtles will be racing with. 
# Moves both turtles at the same pace
def turtleEngine(t, t2, x):
	for k in range(x):
		t.forward(random.randrange(0, 6))
		t2.forward(random.randrange(0, 6))
		
# main function defines the high-level routine.
def main():
  # 2. Create a screen and paint it some interesting color.
  wn = turtle.Screen()
  # color list: https://pythonhosted.org/ete2/_images/svg_colors.png
  wn.bgcolor('papayawhip') 

  # 3. Create a grid to track our turtles' progress.
  dingus = turtle.Turtle()
  dingus.shape("classic")
  # .speed() to avoid wasting the prof's time
  dingus.speed(0)
  drawLine(dingus, -240, 240, 500)
  writeText(dingus, -270, 240, "Start")
  drawDashLine(dingus, -240, 215, 25, 10)

  # 4. Create two turtles with different colors.
  jane = turtle.Turtle()
  jane.color('red')
  jane.shape('turtle')
  joe = turtle.Turtle()
  joe.color('blue')
  joe.shape('turtle')

  # 5. Move the turtles to their starting positions
  moveTurtle(jane, -77.5, 240)
  moveTurtle(joe, 77.5, 240)

  # 6. Send them moving down the screen
  turtleEngine(jane, joe, 175)
  

  # wn.exitonclick()
# execute the program by calling main  
main()
