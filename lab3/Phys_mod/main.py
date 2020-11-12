import turtle
from random import *

turtle.goto(300, 0)
x = -300
y = 0
Vx = 10
Vy = 50
g = -10
dt = 0.05


def main():
    global x, y, Vx, Vy, g, dt

    x += Vx * dt
    y += Vy * dt + g * dt ** 2 / 2
    Vy += g * dt

    if y < 0:
        y = 0
        Vy = 0.8 * abs(Vy)
        Vx *= 0.9

    turtle.goto(x, y)
    main()


try:
    main()
except:
    print("End PM")
