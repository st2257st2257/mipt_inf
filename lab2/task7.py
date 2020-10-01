import numpy as np

import turtle


turtle.speed(1000)
def task6(n,r):
    for i in range(360 * n):
        turtle.forward(1 + i / 350)
        turtle.left((r/20)*1.01)


task6(9,20)
