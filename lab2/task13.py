import numpy as np

import turtle

turtle.speed(1000)

turtle.left(90)


def smile(r=50):
    #face_big

    turtle.color("#ffff00")
    turtle.begin_fill()

    for i in range(360):
        turtle.forward(r/25)
        turtle.right(1)

    turtle.end_fill()

    turtle.color("#000000")

    for i in range(360):
        turtle.forward(r/25)
        turtle.right(1)

    #smile 2.3
    turtle.right(180)
    turtle.penup()
    X, Y = turtle.position()
    turtle.goto(turtle.position()[0] + r*2.3/3, turtle.position()[1] )


    for i in range(120):
        if (i>60)&(i<120):
            turtle.pendown()
            turtle.width(5)
            turtle.color("#ff0000")

            turtle.forward(r*0.0133*2.3*0.9 )
            turtle.left(1)
        else:
            turtle.penup()
            turtle.forward(r*0.0133*2.3*0.9)
            turtle.left(1)
    #

    turtle.penup()

    turtle.goto(X + r * 2.3 * 2/3, Y + r * 2.3 * 1/3)


    turtle.color("#0000ff")
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(r / 200)
        turtle.right(1)

    turtle.end_fill()
    turtle.color("#000000")


    turtle.penup()
    turtle.goto(X + r * 2.3 * 4/ 3, Y + r * 2.3 * 1/3)

    turtle.color("#0000ff")
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(r / 200)
        turtle.right(1)
    turtle.end_fill()
    turtle.color("#000000")

    #
    turtle.penup()
    turtle.goto(X + r * 2.3 , Y - r * 2.3 * 1/6)

    turtle.pendown()
    turtle.width(5)
    turtle.color("#000000")
    turtle.begin_fill()
    turtle.lift(45)
    turtle.forward(r)

    turtle.end_fill()
    turtle.color("#000000")


smile()
