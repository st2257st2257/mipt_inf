import numpy as np

import turtle

turtle.speed(1)

def task5(r,n):
    for i in range(n+1):
        for j in range(i+3):
            turtle.forward(r + i*15)
            turtle.left(360/(i+3))

        turtle.penup()
        turtle.right(90 + 180/(i+3))
        turtle.forward(20)
        turtle.left(90 + 180 / (i + 4))
        turtle.pendown()
task5(60,3)
