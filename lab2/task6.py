import numpy as np

import turtle


turtle.speed(100)
def task6(n,l):
    for i in range(n):
        turtle.forward(l)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(l)
        turtle.left(180 + 360/n)

task6(90,200)
