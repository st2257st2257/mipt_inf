from random import *
import turtle


number_of_turtles = 10
steps_of_time_number = 1000

a, b = 200, 200
turtle.penup()
turtle.goto(a, b)
turtle.pendown()
turtle.goto(a, -b)
turtle.goto(-a, -b)
turtle.goto(-a, b)
turtle.goto(a, b)
turtle.penup()

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
speed = [random()*10 for i in range(number_of_turtles*2)]
for unit in pool:
    unit.penup()
    unit.speed(500)
    unit.shape('circle')
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for counter, unit in enumerate(pool):
        X, Y = unit.position()
        if abs(X) > 200:
            speed[2 * counter] *= (-1)
        if abs(Y) > 200:
            speed[2 * counter+1] *= (-1)

        unit.goto(X+speed[2 * counter], Y+speed[2 * counter+1])
