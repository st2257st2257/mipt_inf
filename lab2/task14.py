import numpy as np

import turtle

turtle.speed(10)

turtle.left(90)


def smile(n,s=1):
    #face_big
    b = 180 - 180*(n-2)/n
    a = 180 - 2*b

    for i in range(n):
        turtle.forward(100)
        if s>0:
            turtle.right(180 - a)
        else:
            turtle.left(180 - a)
    
    if (n%2==0):
        turtle.forward(33)
        turtle.left(a)
        turtle.forward(33)
        turtle.right(2*b)        
        #turtle.forward(33)
        smile(n//2,-s)



smile(5)
