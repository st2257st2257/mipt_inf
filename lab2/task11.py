import numpy as np

import turtle

turtle.speed(100)

def task5(n):
    for i in range(1, n+1):
        for j in range(360):
            turtle.forward(2)
            turtle.left(i)
        turtle.left(180)
        for j in range(360):
            turtle.forward(2)
            turtle.left(i)


task5(3)
