import numpy as np

import turtle

turtle.speed(100)

turtle.left(90)


def task5(n):
    for i in range(1, n+1):
        for j in range(180):
            turtle.forward(2)
            turtle.left(-1)
        #turtle.left(180)


        for j in range(180):
            turtle.forward(0.5)
            turtle.left(-1)


task5(3)
