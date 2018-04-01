# TYLER NEVELL

import turtle
def hw3():
    turtle.setup()
    
    x = input("Enter the amount of sides: ")    
    length = input("Enter the length of the sides: ")
    cline = input("Enter the color of the perimeter: ")
    f = input("Enter the fill color: ")
    
    x = int(x)
    l = int(length)
    
    tot_angle = (x - 2) * 180
    trn = 180 - (tot_angle / x)  
    
    alex = turtle
    alex.color(cline, f)
    alex.begin_fill()
    for t in range(x):
        alex.forward(l)
        alex.left(trn)
        
    alex.end_fill()    
    
    alex.done()
hw3() 
