import numpy as np

import turtle


turtle.speed(100)
def task5(r):
    for i in range(4):
        #turtle.shape('turtle')
        turtle.forward(r)
        turtle.left(90)

for i in range(50):
    task5(i*4)
    #turtle.left(90)
    #turtle.pendown(0)
    turtle.goto(turtle.position()[0] - 2,turtle.position()[1] - 2)
