import numpy as np

import turtle

turtle.speed(100)

def task5(n):
    for i in range(n+1):
        for j in range(360):
            turtle.forward(2)
            turtle.left(1)
        turtle.left(180)
        for j in range(360):
            turtle.forward(2)
            turtle.left(1)
        turtle.left(360/n)

task5(3)
