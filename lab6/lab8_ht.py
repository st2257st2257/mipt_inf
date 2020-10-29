from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))


screen_w = 800
screen_h = 600
grav = 3
number_of_targets = 5


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
    def __init__(self, x=60, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.bouns = 0

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
        self.live = 30

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

        if ((self.x > (screen_w - 20))|(self.x < 50)):
            self.vx *= -0.75
            self.vy *= 0.9
            self.bouns += 1
        if ((self.y > (screen_h - 50))|(self.y < 50)):
            self.vy *= -0.75
            self.vx *= 0.9
            self.bouns += 1

        self.x += self.vx
        self.y -= self.vy
        if (self.bouns < 15):
            canv.coords(self.id, self.x - self.r, (self.y - self.r), self.x + self.r, (self.y + self.r))
        else:
            self.__del__()

    def hittest(self, obj):
      if (((obj.x - self.x)**2 + (obj.y - self.y)**2) < (obj.r + self.r)**2):
            return True
      return False

    def __del__(self):
        canv.delete(self.id)


class Gan():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7) # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text = self.points, font = '28')
        self.new_target()
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)

    def new_target(self):
        x = self.x = rnd(600, screen_w - 100)
        y = self.y = rnd(100, screen_h - 200)
        r = self.r = rnd(2, 25)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def move(self, vx = 0, vy = 0):
        if ((self.x > (screen_w - 50))|(self.x < 50)):
            self.vx *= -1
        if ((self.y > (screen_h - 150))|(self.y < 50)):
            self.vy *= -1

        self.x += self.vx
        self.y += self.vy

        x = self.x
        y = self.y
        r = self.r
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)


    def __del__(self):
        canv.delete(self.id)


Targets = [Target() for i in range( number_of_targets )]
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gan()
bullet = 0
balls = []

def cut(a,n):
    if (len(a)<n):
        pass
    else:
        c_i = len(a)-n
        for i in range(c_i):
            a[0].__del__()
            a.pop(0)
    return a


def new_game(event=''):
    global Gan, screen1, balls, bullet

    #t1.new_target()
    #t2.new_target()


    for t in Targets:
        t.new_target()
        t.live = 1



    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.03
    #t1.live = 1
    #t2.live = 1


    count_T = 0;
    for t in Targets:
        count_T += t.live

    while (count_T) or balls:

        count_T = 0;
        for t in Targets:
            count_T += t.live


        balls = cut(balls, 10)
        for b in balls:
            b.move()
            counter = 0
            for t in Targets:
                t.move()
                if (b.hittest(t) and t.live):
                    t.live = 0
                    t.hit()
                    Targets.pop(counter)
                    canv.itemconfig(screen1, text='You hit it by ' + str(bullet) + ' shots')
                counter += 1
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(Gan)
    root.after(750, new_game)


new_game()
mainloop()
