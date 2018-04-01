# TYLER NEVELL

import turtle as t
def main():
    
    colors = ['red', 'blue', 'yellow', 'green', 'pink']
    i = 0
    x = 5
    t.pensize(3)
    for u in range(50):
        c = i % len(colors)
        t.pencolor(colors[c])
        i = i + 1
        t.forward(x)
        t.left(90)
        x = x + 5
        
main()
t.exitonclick()