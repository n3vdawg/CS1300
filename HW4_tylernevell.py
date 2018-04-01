# 1. Import the needed modules
import turtle
import random

# create a function that moves turtles to starting position and draws a line
def drawLine(t, x, y, l):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(l)
# create a function that writes text with a turtle
def writeText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(str(text))
    
#Create a function that will draw a dashed line
def drawDashLine(t, x, y, dashLength, numDashes):
    for t in (numDashes):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(dashLength)
        

# main function defines the high-level routine.
def main():
  # 2. Create a screen and paint it some interesting color.
  wn = turtle.Screen()
  # color list: https://pythonhosted.org/ete2/_images/svg_colors.png
  wn.bgcolor('papayawhip') 

  # 3. Create a grid to track our turtles' progress.
  dingus = turtle.Turtle()
  dingus.shape("classic")
  drawLine(dingus, -240, 240, 500)
  writeText(dingus, -270, 240, "Start")
  drawDashLine(dingus, -240, 215, 25, 10)

  # 4. Create two turtles with different colors.
  jane = turtle.Turtle()
  jane.color('red')
  jane.shape('turtle')
  joe  = turtle.Turtle()
  joe.color('blue')
  joe.shape('turtle')

  # 5. Move the turtles to their starting positions
  # TODO

  # 6. Send them moving down the screen
  # TODO
  

  # The following line is not needed if you're using repl.it:
  wn.exitonclick()


# execute the program by calling main  
main()