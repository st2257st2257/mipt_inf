import turtle
from random import *


x = 0
y = 200
vx = 30
vy = 0
g = 3

def main():
    vy -= g
    if y < 0:
        y = 0
        vy = abs(vy)

    turtle.goto(x + vx, y + vy)
    main()


main()
