import turtle
from random import *

e_file = open("file name",'r') #"0,0,10,0#10,0,10,10#10,10,10,20#10,20,0,20#0,20,0,10#0,10,0,0#0,10,10,10#0,20,10,10#0,10,10,0"
s_file = open("file name",'r') #"1,2,3,4,5,6#9,2,3#1,2,8,4#1,9,7,8#6,7,2,3#1,6,7,3,4#9,5,4,3,7#1,9,5#1,2,3,4,5,6,7#1,2,7,6,8"

numbers = open("file name",'r').read().split(',')

str_e,str_n = e_file.read(),s_file.read()

#str_elments,str_numbers = str_e,str_n

#              1        2          3          4           5        6         7           8
str_elments = "0,0,10,0#10,0,10,10#10,10,10,20#10,20,0,20#0,20,0,10#0,10,0,0#0,10,10,10#0,20,10,10#0,10,10,0"
str_numbers = "1,2,3,4,5,6#9,2,3#1,2,8,4#1,9,7,8#6,7,2,3#1,6,7,3,4#9,5,4,3,7#1,9,5#1,2,3,4,5,6,7#1,2,7,6,8"

def elment(i,s):
    elms = str_elments.split('#')
    coord = []
    for e in range(len(elms)):
        coord.append(elms[e].split(','))


    x1,y1,x2,y2 = int(coord[i-1][0])+s, int(coord[i-1][1]), int(coord[i-1][2])+s, int(coord[i-1][3])
    print(x1,y1,x2,y2)
    turtle.penup()
    turtle.goto(x1,-y1)
    turtle.pendown()
    turtle.goto(x2, -y2)
    turtle.penup()

def numb(n,s):
    elms = str_numbers.split('#')

    coord = []
    for i in range(len(elms)):
        vel = elms[i].split(',')
        coord.append(vel)
    print(coord)


    for j in range(len(coord[n])):
        elment(int(coord[n][j]),s)
        print(coord[n][j])

def out(a):
    for i in range(len[a]):
        numb(a[i], i*30)


# start:
#out(nubmers);
