import numpy as np

import turtle


turtle.speed(10)

counter = 0;
def task5(r):
    global counter
    for i in range(4):
        #turtle.shape('turtle')

        turtle.forward(r + counter)
        turtle.left(90)
        counter += 1

for i in range(50):
    task5(i*4)
    #turtle.left(90)
    #turtle.pendown(0)
    turtle.goto(turtle.position()[0] - 2,turtle.position()[1] - 2)
