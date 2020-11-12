import turtle

e_file = open("e_file.txt", 'r')
s_file = open("s_file.txt", 'r')
numbers = open("name.txt", 'r').read()[:-1:].split(' ')

str_e, str_n = e_file.read(), s_file.read()

str_elments = str_e
str_numbers = str_n
print(str_elments)


def elment(i, s):
    elms = str_elments.split('#')
    coord = []
    for e in range(len(elms)):
        coord.append(elms[e].split(','))

    x1, y1, x2, y2 = int(coord[i-1][0])+s, int(coord[i-1][1]), int(coord[i-1][2])+s, int(coord[i-1][3])
    print(x1, y1, x2, y2)
    turtle.penup()
    turtle.goto(x1, -y1)
    turtle.pendown()
    turtle.goto(x2, -y2)
    turtle.penup()


def numb(n, s):
    elms = str_numbers.split('#')

    coord = []
    for i in range(len(elms)):
        vel = elms[i].split(',')
        coord.append(vel)
    print(coord)

    for j in range(len(coord[n])):
        elment(int(coord[n][j]), s)
        print(coord[n][j])


def out(a):
    for i in range(len(a)):
        numb(int(a[i]), i*30)


# start:
out(numbers)
