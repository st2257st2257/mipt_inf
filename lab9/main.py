from random import randrange as rnd, choice
import tkinter as tk
import math
import time

"""  base constants  """
screen_w = 1200
screen_h = 600
border_x = 50
border_y = 50

grav = 1
number_of_targets = 5
k_fire = 1
k_hard = 1.0001
k_acct = 1.2
number_of_shorts = 0
number_of_liders = 10

test_user_name = "ask"

bullet = 0
balls = []
clicks = 0


"""  base settings  """
root = tk.Tk()
fr = tk.Frame(root)
root.geometry(str(screen_w) + 'x' + str(screen_h+30))
canv = tk.Canvas(root, bg='SkyBlue')
canv.pack(fill=tk.BOTH, expand=1)

settings = tk.Tk()
# fr = tk.Frame(settings)
settings.geometry('400x250')


"""  base classes  """


class GameObject:
    def __init__(self, x=0, y=0,
                 x_l=0, y_l=0,
                 vx=0, vy=0,
                 mirror=1,
                 live=0,
                 name="",
                 color=''):
        """
        :param x:      position of the object OX
        :param y:      position of the object OY
        :param x_l:    normal vector OX
        :param y_l:    normal vector OY
        :param mirror: mirror
        :param vx:     velocity OX
        :param vy:     velocity OY
        """
        self.x = x
        self.y = y

        self.x_l = x_l
        self.y_l = y_l

        self.vx = vx
        self.vy = vy

        self.mirror = mirror
        self.live = live
        self.name = name
        self.color = color

    def print(self):
        print("Printing Game Object: ")
        print("Name: " + self.name)
        print("(Coord) x:" + str(self.x) + " y:" + str(self.y))
        print("(Velocity) vx:" + str(self.vx) + " vy:" + str(self.vy))
        print("(Guiding Vector) x_l:" + str(self.x_l) + " y_l:" + str(self.y_l))
        print("Mirror: " + str(self.mirror))
        print("Live: " + str(self.live))
        print("Color: " + str(self.color))

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def __del__(self):
        pass


class Ball(GameObject):
    def __init__(self, x=60, y=450):
        super().__init__(x=x, y=y, vx=0, vy=0, live=30)

        self.r = 10
        self.bouns = 0
        self.fire = 1
        self.type = ''

        self.color = choice(['blue',
                             'green',
                             'yellow',
                             'cyan',
                             'silver',
                             'black',
                             'fuchsia',
                             'lime',
                             'peru',
                             'brown'])

        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        self.vy -= grav

        if (self.x > (screen_w - border_x + 10)) | (self.x < border_x - 10):
            self.vx *= -0.75
            self.vy *= 0.9
            self.bouns += 1
        if (self.y > (screen_h - border_y + 10)) | (self.y < border_y - 10):
            self.vy *= -0.75
            self.vx *= 0.9
            self.bouns += 1

        self.x += self.vx
        self.y -= self.vy
        if self.bouns < 15:
            canv.coords(self.id, self.x - self.r, (self.y - self.r), self.x + self.r, (self.y + self.r))
        else:
            self.__del__()

    def hittest(self, obj):
        if ((obj.x - self.x)**2 + (obj.y - self.y)**2) < (obj.r + self.r)**2:
            return True
        return False

    def __del__(self):
        canv.delete(self.id)
        self.x = -100
        self.y = -100


class Gan(GameObject):
    def __init__(self, x=20, y=50, color='black', ttype=''):
        super().__init__(x=x, y=y, live=100, color=color)

        self.type = ttype
        self.turn_on = 1
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(x, y, x+30, y-30, width=7)

    def fire2_start(self, event):
        if self.turn_on:
            global number_of_shorts
            self.f2_on = 1
            number_of_shorts += 1

    """ I """""" II """""" III """""" VI """
    def update_an(self, event):
        pi = 3.14
        if ((event.x - self.x) > 0) & ((event.y - self.y) > 0):
            self.an = abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) < 0) & ((event.y - self.y) > 0):
            self.an = pi - abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) < 0) & ((event.y - self.y) < 0):
            self.an = -pi + abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) > 0) & ((event.y - self.y) < 0):
            self.an = -abs(math.atan((event.y - self.y) / (event.x - self.x)))
        self.an *= -1

    def fire2_end(self, event):
        global balls, bullet
        if self.turn_on:
            bullet += 1
            new_ball = Ball()
            new_ball.r += 5
            new_ball.type = self.type

            self.update_an(event)

            new_ball.x = min(max(self.x + max(self.f2_power, 20) * math.cos(
                self.an), border_x), screen_w - border_x)
            new_ball.y = min(max(self.y + max(self.f2_power, 20) * math.sin(
                self.an), border_x), screen_h - border_y)
            new_ball.vx = k_fire * self.f2_power * math.cos(self.an)
            new_ball.vy = k_fire * self.f2_power * math.sin(self.an)
            balls += [new_ball]

            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
            self.update_an(event)

            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event=0):
        if self.turn_on:
            if event:
                self.update_an(event)
            if self.f2_on:
                canv.itemconfig(self.id, fill='orange')
            else:
                canv.itemconfig(self.id, fill=self.color)

            canv.coords(self.id, self.x, self.y,
                        self.x + max(self.f2_power, 20) * math.cos(self.an),
                        self.y - max(self.f2_power, 20) * math.sin(self.an)
                        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, self.x + self.vx, self.y + self.vy,
                    self.x + self.vx + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + self.vy - max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill=self.color)


class Gans:
    def __init__(self, arr):
        self.gans = []
        self.fire_gan = 0

        for g in arr:
            self.gans.append(g)

    def add(self, gan):
        self.gans.append(gan)

    def fire2_start(self, event):
        self.gans[self.fire_gan].fire2_start(event)

    def fire2_end(self, event):
        self.gans[self.fire_gan].fire2_end(event)

    def targetting(self, event=0):
        self.gans[self.fire_gan].targetting(event)

    def power_up(self):
        self.gans[self.fire_gan].power_up()

    def __del__(self):
        for gan in self.gans:
            canv.delete(gan.id)


class Tank(GameObject):
    def __init__(self, x=0, y=0, live=0, name='Tank',  vx=0, vy=0, ttype=''):
        super().__init__(x=x, y=y, live=live, name=name, vx=vx, vy=vy)
        self.n_whells = 5
        self.lenght = 40
        self.live = 20
        self.ttype = type
        self.platform_id = canv.create_rectangle(x, y, x + self.lenght, y + self.lenght/4, fill='green')
        self.tower = canv.create_rectangle(x + self.lenght/3,
                                           y,
                                           x + 2*self.lenght/3,
                                           y - self.lenght/8, fill='green')

        self.whells = [canv.create_oval(
                self.x + i*self.lenght/self.n_whells - self.lenght/(self.n_whells*2),
                self.y + 10 - self.lenght/(self.n_whells*2),
                self.x + i*self.lenght/self.n_whells + self.lenght/(self.n_whells*2),
                self.y + 10 + self.lenght/(self.n_whells*2),
                fill='black') for i in range(self.n_whells)]

        self.live_bar_all = canv.create_rectangle(x, y-5, x + 10, y - 7, fill='red')
        self.live_bar = canv.create_rectangle(x, y-5, x + 10*(self.live/20), y - 7, fill='green')

        self.gan = Gan(x + int(self.lenght/2), y, color='black', ttype=ttype)

    def move(self):
        if self.gan.turn_on:
            if (self.x > (screen_w - 50)) | (self.x < 50):
                self.vx *= -1
            if (self.y > (screen_h - 150)) | (self.y < 50):
                self.vy *= -1

            self.x += self.vx
            self.y += self.vy
            self.gan.vx = self.vx
            self.gan.vy = self.vy
            self.gan.move()

            canv.coords(self.platform_id, self.x + self.vx,
                        self.y + self.vy,
                        self.x + self.vx + self.lenght,
                        self.y + self.vy + self.lenght/4)
            canv.coords(self.tower,
                        self.x + self.lenght/3 + self.vx,
                        self.y + self.vy,
                        self.x + 2 * self.lenght / 3 + self.vx,
                        self.y - self.lenght / 8 + self.vy)

            canv.coords(self.live_bar_all,
                        self.x + self.vx,
                        self.y - 5 + self.vy,
                        self.x + 10 + self.vx,
                        self.y - 7 + self.vy)

            canv.coords(self.live_bar,
                        self.x + self.vx,
                        self.y - 5 + self.vy,
                        self.x + max(10*(self.live/20), 0) + self.vx,
                        self.y - 7 + self.vy)

            for i, w in enumerate(self.whells):
                canv.coords(w, self.x + self.vx + i*self.lenght/self.n_whells,
                            self.y + self.vy + 10 - self.lenght/(self.n_whells*2),
                            self.x + self.vx + i*self.lenght/self.n_whells + self.lenght / self.n_whells,
                            self.y + self.vy + 10 + self.lenght/(self.n_whells*2))

    def hittest(self, oobject):
        if (abs(abs(int((self.x-oobject.x)) ^ 2) + abs(int((self.y-oobject.y)) ^ 2))
                < int((self.lenght/2 + oobject.r)) ^ 2) & (oobject.type != self.ttype):
            print(oobject.x, oobject.y)
            print(self.x, self.y)
            print(abs(int((self.x-oobject.x)) ^ 2 + int((self.y-oobject.y)) ^ 2))
            print(int((self.lenght/2 + oobject.r)) ^ 2)

            print("hit " + oobject.color + " to " + self.name)
            self.live -= oobject.fire
            oobject.__del__()

            if self.live == 0:
                self.vx = 0
                self.vy = 0
                self.gan.turn_on = 0


class Plane(GameObject):
    def __init__(self, x=0, y=0, live=0, name='Plane',  vx=0, vy=0, ttype='Plane'):
        super().__init__(x=x, y=y, live=live, name=name, vx=vx, vy=vy)

        self.lenght = 40
        self.n_windows = 4
        self.r = self.lenght/2
        self.type = ttype

        self.box = canv.create_rectangle(x - self.lenght/2, y,
                                         x + self.lenght/2, y - self.lenght/8,
                                         fill='white')

        self.mirror = 1
        self.wings_form = canv.create_line(self.x + self.mirror * self.lenght/4,
                                           self.y - 3*self.lenght/8,
                                           self.x - self.mirror * self.lenght/4,
                                           self.y + self.lenght/4,
                                           width=self.lenght/8,
                                           fill='black')

        self.wings = canv.create_line(self.x + self.mirror * self.lenght / 4,
                                      self.y - 3*self.lenght / 8,
                                      self.x - self.mirror * self.lenght / 4,
                                      self.y + self.lenght / 4,
                                      width=self.lenght / 10,
                                      fill='white'
                                      )

        self.cabin = canv.create_oval(self.x + self.mirror * 3 * self.lenght/8,
                                      self.y - self.lenght/8,
                                      self.x + self.mirror * 5 * self.lenght/8,
                                      self.y,
                                      fill='white')

        self.tail_form = canv.create_line(self.x - self.mirror * self.lenght/2,
                                          self.y,
                                          self.x - self.mirror * 3 * self.lenght/4,
                                          self.y - self.lenght/4,
                                          width=self.lenght / 8,
                                          fill='black')

        self.tail = canv.create_line(self.x - self.mirror * self.lenght / 2,
                                     self.y,
                                     self.x - self.mirror * 3 * self.lenght / 4,
                                     self.y - self.lenght / 4,
                                     width=self.lenght / 10,
                                     fill='white')

        self.windows = [canv.create_oval(
            self.x - self.lenght / 2 + i * self.lenght / self.n_windows,
            self.y - 2 * self.lenght / 24,
            self.x - self.lenght / 2 + i * self.lenght / self.n_windows + self.lenght / 24,
            self.y - self.lenght / 24,
            fill='black') for i in range(self.n_windows)]

        self.live_bar_all = canv.create_rectangle(x, y-5, x + 10, y - 7, fill='red')
        self.live_bar = canv.create_rectangle(x, y-5, x + 10*(self.live/20), y - 7, fill='green')

        self.gan = Gan(x=x, y=y, color='Gray', ttype=self.type)

    def move(self):
        self.live = min(self.live, 10)
        if self.gan.turn_on:
            if (self.x > (screen_w - 50)) | (self.x < 50):
                self.vx *= -1
                self.mirror *= -1
            if (self.y > 150) | (self.y < 50):
                self.vy *= -1

            self.x += self.vx
            self.y += self.vy
            self.gan.vx = self.vx
            self.gan.vy = self.vy
            self.gan.move()

            canv.coords(self.box, self.x - self.lenght / 2 + self.vx,
                        self.y + self.vy,
                        self.x + self.lenght / 2 + self.vx,
                        self.y - self.lenght / 8 + self.vy)

            canv.coords(self.wings_form, self.x + self.mirror * self.lenght / 4 + self.vx,
                        self.y - 3 * self.lenght / 8 + self.vy,
                        self.x - self.mirror * self.lenght / 4 + self.vx,
                        self.y + self.lenght / 4 + self.vy)

            canv.coords(self.wings, self.x + self.mirror * self.lenght / 4 + self.vx,
                        self.y - 3 * self.lenght / 8 + self.vy,
                        self.x - self.mirror * self.lenght / 4 + self.vx,
                        self.y + self.lenght / 4 + self.vy)

            canv.coords(self.cabin, self.x + self.vx + self.mirror * 3 * self.lenght / 8,
                        self.y - self.lenght / 8 + self.vy,
                        self.x + self.mirror * 5 * self.lenght / 8 + self.vx,
                        self.y + self.vy)

            canv.coords(self.tail_form, self.x - self.mirror * self.lenght / 2 + self.vx,
                        self.y + self.vy,
                        self.x + self.vx - self.mirror * 3 * self.lenght / 4,
                        self.y + self.vy - self.lenght / 4)

            canv.coords(self.tail, self.x - self.mirror * self.lenght / 2 + self.vx,
                        self.y + self.vy,
                        self.x + self.vx - self.mirror * 3 * self.lenght / 4,
                        self.y + self.vy - self.lenght / 4)

            canv.coords(self.live_bar_all,
                        self.x + self.vx - 15,
                        self.y - 5 + self.vy - 5,
                        self.x + 10 + self.vx - 15,
                        self.y - 7 + self.vy - 5)

            canv.coords(self.live_bar,
                        self.x + self.vx - 15,
                        self.y - 5 + self.vy - 5,
                        self.x + max(10*(self.live/10), 0) + self.vx - 15,
                        self.y - 7 + self.vy - 5)

            for (i, w) in enumerate(self.windows):
                canv.coords(w,
                            self.x + self.vx - self.lenght / 2 + i * self.lenght / self.n_windows,
                            self.y + self.vy - 2 * self.lenght / 24,
                            self.x + self.vx - self.lenght / 2 + i * self.lenght / self.n_windows + self.lenght / 24,
                            self.y - self.lenght / 24)

    def hittest(self, oobject):
        if (abs(abs(int((self.x-oobject.x)) ^ 2) + abs(int((self.y-oobject.y)) ^ 2))
                < int((self.lenght/2 + oobject.r)) ^ 2) & (oobject.type != self.type):
            print(oobject.x, oobject.y)
            print(self.x, self.y)

            print(abs(int((self.x-oobject.x)) ^ 2 + int((self.y-oobject.y)) ^ 2))
            print(int((self.lenght/2 + oobject.r)) ^ 2)

            print("hit " + oobject.color + " to " + self.name)
            self.live -= oobject.fire
            oobject.__del__()

            if self.live == 0:
                self.vx = 0
                self.vy = 0
                self.gan.turn_on = 0


T = Tank(x=100, y=screen_h-100, live=100, vx=5, ttype='t1')
TT = Tank(x=1000, y=screen_h-100, live=100, vx=-2, ttype='t2')

P = Plane(x=400, y=100, live=10, vx=5, vy=1)


class Lider(GameObject):
    def __init__(self, name="", count=0):
        self.place = 1000
        super().__init__(x=screen_w-100, y=100+15*self.place, live=30, name=name)
        self.count = count
        self.id = canv.create_text(self.x, self.y, text=self.name + "   " + str(float(self.count))[:5])

    def add(self, value):
        self.count += value
        canv.delete(self.id)
        self.id = canv.create_text(screen_w-100, 30+15*self.place, text=self.name + "   " + str(float(self.count))[:5])

    def __del__(self):
        canv.delete(self.id)


class LiderBoard:
    def __init__(self, data):
        global number_of_liders
        self.max_n = number_of_liders

        self.arr = [Lider(name=data[i][0], count=float(data[i][1][0:5])) for i in range(len(data))]
        self.arr = sorted(self.arr, key=lambda liderr: -liderr.count)

        for i in range(len(self.arr)):
            self.arr[i].place = i

    def sort(self):
        self.arr = sorted(self.arr, key=lambda lider: -lider.count)

    def update_board(self):
        self.sort()
        for i in range(len(self.arr)):
            self.arr[i].place = i
            canv.coords(self.arr[i].id, screen_w-100, 100+self.arr[i].place*15)

    def add_lider(self, user_name, count):
        self.arr.append(Lider(user_name, count))
        self.update_board()

    def add_score(self, score):
        for LL in self.arr:
            if LL.name == test_user_name:
                print("hit")
                print(LL.name, " ", LL.count)
                LL.add(score)
        for LL in self.arr:
            print(LL.count, LL.place)
        self.update_board()

    def __del__(self):
        if 'self.arr' in locals():
            for i in range(len(self.arr)):
                canv.delete(self.arr[i].id)


class Target(GameObject):
    def __init__(self):

        super().__init__(x=rnd(600, screen_w - 100), y=rnd(100, screen_h - 200),
                         vx=rnd(-10, 10), vy=rnd(-10, 10), live=1, color='red')

        self.r = rnd(2, 25)
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points)
        self.new_target()

    def new_target(self):
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self, vx=0, vy=0):
        if (self.x > (screen_w - 50)) | (self.x < 50):
            self.vx *= -1
        if (self.y > (screen_h - 150)) | (self.y < 50):
            self.vy *= -1

        self.vx *= k_hard
        self.vy *= k_hard

        self.x += self.vx
        self.y += self.vy

        x = self.x
        y = self.y
        r = self.r
        # color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)

    def __del__(self):
        try:
            canv.delete(self.id)
        except 1:
            pass


"""  create main objects of the game  """
Targets = [Target() for i in range(number_of_targets)]
screen1 = canv.create_text(400, 300, text='', font='28')

g2 = Gan(50, screen_h-100)
g3 = Gan(x=50, y=50, color='green')
g4 = Gan(screen_w-100, screen_h-100)
g5 = Gan(screen_w-100, 50)


g1 = Gans([P.gan, g2, g3, g5, g4, T.gan, TT.gan])

"""  base functions  """


def click_button(index=0):
    global k_hard, bullet
    bullet = 0
    cou = len(Targets)
    for i in range(cou):
        Targets[-1].__del__()
        Targets.pop(-1)
    if index == 0:
        k_hard = 1
        P.gan.turn_on = 1
        P.live = 20
        P.vx = 2*P.mirror
        P.vy = 1
        T.gan.turn_on = 1
        T.live = 20
        T.vx = 3
        TT.gan.turn_on = 1
        TT.live = 20
        TT.vx = -3
    else:
        pass

    for j in range(number_of_targets):
        Targets.append(Target())


def acceleration_button():
    for b in balls:
        b.vx *= k_acct
        b.vy *= k_acct
    print("acceleration")


def change_gan():
    g1.fire_gan = (g1.fire_gan+1) % len(g1.gans)


def get_users():
    gamers = open("newtext.txt", 'r')
    data_p = gamers.read()[:-1].split(';')

    data = [data_p[i].split(',') for i in range(len(data_p))]
    gamers.close()
    return data


def move_t_right(event):
    global T
    T.vx += 1


def move_t_left(event):
    global T
    T.vx -= 1


def move_tt_right(event):
    global TT
    TT.vx += 1


def move_tt_left(event):
    global TT
    TT.vx -= 1


def move_p_right(event):
    global TT
    TT.vx += 1


def move_p_left(event):
    global TT
    TT.vx -= 1


def set_users(Data):
    gamers = open("newtext.txt", 'w')
    gamers.write(Data)
    gamers.close()


def cut(a, n):
    if len(a) < n:
        pass
    else:
        c_i = len(a)-n
        for i in range(c_i):
            a[0].__del__()
            a.pop(0)
    return a


LB = LiderBoard(get_users())
LB.update_board()


def qquit(rooot):
    rooot.destroy()


"""  settings window  """
tk.Button(settings, text="Quit",  background="#ff3333", foreground="#ccc", padx="16", pady="16",
          command=lambda settings=settings: qquit(settings)).pack(side="right")

rad1 = tk.Radiobutton(settings, text='Первый', value=1)
rad2 = tk.Radiobutton(settings, text='Второй', value=2)
rad3 = tk.Radiobutton(settings, text='Третий', value=3)
rad1.pack()
rad2.pack()
rad3.pack()

tk.Button(root, text="Quit",  background="#ff3333", foreground="#ccc", padx="16", pady="16",
          command=lambda root=root: qquit(root)).pack(side="right")

btn = tk.Button(text="Restart", background="#555", foreground="#ccc",
                padx="40", pady="16", command=click_button)
btn.pack(side="right")


btn = tk.Button(text="Acceleration", background="#555", foreground="#ccc",
                padx="40", pady="16", command=acceleration_button)
btn.pack(side="right")

btn = tk.Button(text="Change", background="#555", foreground="#ccc",
                padx="40", pady="16", command=change_gan)
btn.pack(side="right")


def new_game():
    try:
        global screen1, balls, bullet, k_hard

        for t in Targets:
            t.new_target()
            t.live = 1

        bullet = 0
        balls = []
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)
        canv.bind('<Motion>', g1.targetting)

        root.bind('d', move_t_right)
        root.bind('a', move_t_left)

        root.bind('m', move_tt_right)
        root.bind('b', move_tt_left)

        root.bind('<Right>', move_p_right)
        root.bind('<Left>', move_p_left)

        count_ttt = 0
        for t in Targets:
            count_ttt += t.live

        while count_ttt or balls or 1:
            T.move()
            TT.move()
            P.move()

            LB.update_board()

            if len(Targets) == 0:
                click_button(1)

            count_t = 0
            for t in Targets:
                count_t += t.live

            balls = cut(balls, 10)

            for (i, b) in enumerate(balls):
                T.hittest(b)
                TT.hittest(b)
                P.hittest(b)

                b.move()
                counter = 0
                for t in Targets:
                    if b.hittest(t) and t.live:
                        k_hard *= k_hard
                        t.live = 0
                        t.hit()
                        LB.add_score((10/(t.r * math.sqrt(number_of_shorts))) * math.sqrt(t.vx*t.vx + t.vy *
                                     t.vy) / 50)
                        Targets.pop(counter)
                    counter += 1

            for t in Targets:
                t.move()

            canv.update()
            time.sleep(0.03)
            g1.targetting()
            g1.power_up()
        canv.itemconfig(screen1, text='')
        canv.delete(Gan)
        root.after(750, new_game)
    except:
        pass


new_game()

res_arr = ""
for L in LB.arr:
    res_arr += (str(L.name) + ',' + str(L.count)[0:5] + ";")
root.mainloop()

set_users(res_arr)

print(res_arr[:-1])
