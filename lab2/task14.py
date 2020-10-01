import numpy as np

import turtle

turtle.speed(10)

turtle.left(90)


def smile(n):
    #face_big
    b = 180 - 180*(n-2)/n
    a = 180 - 2*b

    for i in range(n):
        turtle.forward(100)
        turtle.right(180 - a)



smile(5)
