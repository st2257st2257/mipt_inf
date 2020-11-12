from random import randrange as rnd, choice
import tkinter as tk
#import numpy as np
import tkinter.font as font
import math
import time




"""  base constants  """
screen_w = 800
screen_h = 800
border_x = 50
border_y = 50

grav = 1
number_of_targets = 5
k_fire = 1
k_hard = 1.0002
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
root.geometry(str (screen_w) + 'x' + str(screen_h+30))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

settings = tk.Tk()
fr = tk.Frame(settings)
settings.geometry('400x250')

"""  base classes  """
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

        if ((self.x > (screen_w - border_x + 10))|(self.x < border_x - 10 )):
            self.vx *= -0.75
            self.vy *= 0.9
            self.bouns += 1
        if ((self.y > (screen_h - border_y + 10))|(self.y < border_y - 10)):
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
    def __init__(self,x = 20, y = 450):
        self.x = x
        self.y = y
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(x, y, x+30, y-30, width=7)
        self.under_pi_div_2 = 1

    def fire2_start(self, event):
        global number_of_shorts
        self.f2_on = 1
        number_of_shorts += 1

    """ I """""" II """""" III """""" VI """
    def update_an(self, event):
        pi = 3.14
        if ((event.x - self.x) > 0)&((event.y - self.y) > 0):
            self.an = abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) < 0)&((event.y - self.y) > 0):
            self.an = pi - abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) < 0) & ((event.y - self.y) < 0):
            self.an = -pi + abs(math.atan((event.y - self.y) / (event.x - self.x)))
        elif ((event.x - self.x) > 0) & ((event.y - self.y) < 0):
            self.an = -abs(math.atan((event.y - self.y) / (event.x - self.x)))
        self.an *= -1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5

        new_ball.vx = k_fire * self.f2_power * math.cos(self.an)
        new_ball.vy = - k_fire * self.f2_power * math.sin(self.an)
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))

        if ((event.x - self.gans[self.fire_gan].x) > 0):
            self.under_pi_div_2 = 1
        else:
            self.under_pi_div_2 = -1

        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        if event:
            self.an = -math.atan((event.y-self.y) / (event.x-self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
            #print(9)
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )
        print(self.x, self.y)


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

class Gans:
    def __init__(self, arr= []):
        self.gans = []
        self.fire_gan = 0


        for g in arr:
            self.gans.append(g)

    def add(self, gan):
        self.gans.append(gan)

    def fire2_start(self, event):
        global number_of_shorts
        self.gans[self.fire_gan].f2_on = 1
        number_of_shorts += 1

    def fire2_end(self, event):
        global balls, bullet

        bullet += 1
        new_ball = Ball()
        new_ball.r += 5

        self.gans[self.fire_gan].update_an(event)



        new_ball.x = min(max(self.gans[self.fire_gan].x + max(self.gans[self.fire_gan].f2_power, 20) * math.cos(self.gans[self.fire_gan].an), border_x), screen_w - border_x)
        new_ball.y = min(max(self.gans[self.fire_gan].y + max(self.gans[self.fire_gan].f2_power, 20) * math.sin(self.gans[self.fire_gan].an), border_x), screen_h - border_y)
        new_ball.vx = k_fire * self.gans[self.fire_gan].f2_power * math.cos(self.gans[self.fire_gan].an)
        new_ball.vy = k_fire * self.gans[self.fire_gan].f2_power * math.sin(self.gans[self.fire_gan].an)
        balls += [new_ball]



        self.gans[self.fire_gan].an = math.atan((event.y - new_ball.y) / (0.001 + event.x - new_ball.x))
        self.gans[self.fire_gan].update_an(event)


        self.gans[self.fire_gan].f2_on = 0
        self.gans[self.fire_gan].f2_power = 10

    def targetting(self, event=0):
        if event:
            self.gans[self.fire_gan].update_an(event)
        if self.gans[self.fire_gan].f2_on:
            canv.itemconfig(self.gans[self.fire_gan].id, fill='orange')
            # print(9)
        else:
            canv.itemconfig(self.gans[self.fire_gan].id, fill='black')

        canv.coords(self.gans[self.fire_gan].id, self.gans[self.fire_gan].x, self.gans[self.fire_gan].y,
                    self.gans[self.fire_gan].x + self.gans[self.fire_gan].under_pi_div_2 * max(self.gans[self.fire_gan].f2_power, 20) * math.cos(self.gans[self.fire_gan].an),
                    self.gans[self.fire_gan].y - max(self.gans[self.fire_gan].f2_power, 20) * math.sin(self.gans[self.fire_gan].an)
                    )


    def power_up(self):
        if self.gans[self.fire_gan].f2_on:
            if self.gans[self.fire_gan].f2_power < 100:
                self.gans[self.fire_gan].f2_power += 1
            canv.itemconfig(self.gans[self.fire_gan].id, fill='orange')
        else:
            canv.itemconfig(self.gans[self.fire_gan].id, fill='black')





    def __del__(self):
        for gan in self.gans:
            canv.delete(gan.id)

class Lider():
    def __init__(self, name="", count = 0):
        self.name = name
        self.count = count
        self.place = 1000
        self.id = canv.create_text(screen_w-100, 100+15*self.place, text =  self.name + "   " + str(float(self.count))[:5])

    def add(self, value):
        self.count += value
        canv.delete(self.id)
        self.id = canv.create_text(screen_w-100, 30+15*self.place, text =  self.name + "   " + str(float(self.count))[:5])

    def __del__(self):
        canv.delete(self.id)

class LiderBoard():
    def __init__(self, Data):
        global number_of_liders
        self.max_n = number_of_liders

        self.arr = [Lider(name = Data[i][0], count = float(Data[i][1][0:5])) for i in range(len(Data))]

        #self.arr.append(Lider(name = "user24", count = 3))   )

        self.arr = sorted(self.arr, key = lambda lider: -lider.count)

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
        self.arr.append(Lider(user_name,count))
        self.update_board()

    def add_score(self, lider_name, score):
        for L in self.arr:
            if (L.name == test_user_name):
                print("hit")
                print(L.name, " ", L.count)
                L.add(score)
        for L in self.arr:
            print(L.count, L.place)
        self.update_board()

    def __del__(self):
        if 'self.arr' in locals():
            for i in range(len(self.arr)):
                canv.delete(self.arr[i].id)

class Target():
    def __init__(self):
        self.points = 0
        self.live = 1
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text = self.points)
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


        self.vx *= k_hard
        self.vy *= k_hard

        self.x += self.vx
        self.y += self.vy

        x = self.x
        y = self.y
        r = self.r
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        #canv.coords(self.id, x - r, y - r, self.vx, self.vy)


    def __del__(self):
        try:
            canv.delete(self.id)
        except:
            pass


"""  create main objects of the game  """
Targets = [Target() for i in range( number_of_targets )]
screen1 = canv.create_text(400, 300, text='', font='28')

g2 = Gan(50,screen_h-100)
g3 = Gan(50,50)
g4 = Gan(screen_w-100,screen_h-100)
g5 = Gan(screen_w-100,50)


g1 = Gans([g2,g3,g5,g4])





"""  base functions  """

def click_button(index = 0):
    global k_hard, bullet
    bullet = 0
    cou = len(Targets)
    for i in range(cou):
        Targets[-1].__del__()
        Targets.pop(-1)
    if (index == 0):
        k_hard = 1
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
    g1.fire_gan = (g1.fire_gan+1)%len(g1.gans)

#read data
def get_users():
    gamers = open("newtext.txt", 'r')

    #print(gamers.read())
    Data_p = gamers.read()[:-1].split(';')
    #print(len(Data_p))

    Data = [Data_p[i].split(',')  for i in range(len(Data_p))]
    gamers.close()
    #for e in Data:
    #    print(e)
    #print(len(Data))
    return Data

#write data
def set_users(Data):
    gamers = open("newtext.txt", 'w')
    res = ""
    #for i in range(len(Data)):
    #    res += str(Data[i][0]) \
    #           + "," \
    #           + str(Data[i][1]) + ';'
    #gamers.write(res[:-1:])

    gamers.write(Data)
    gamers.close()

def cut(a,n):
    if (len(a)<n):
        pass
    else:
        c_i = len(a)-n
        for i in range(c_i):
            a[0].__del__()
            a.pop(0)
    return a

LB = LiderBoard(get_users())
LB.update_board()


def quit(root):
    root.destroy()


"""  settings window  """
tk.Button(settings, text="Quit",  background="#ff3333", foreground="#ccc", padx="16", pady="16", command=lambda settings=settings:quit(settings)).pack(side = "right")

rad1 = tk.Radiobutton(settings, text='Первый', value=1)
rad2 = tk.Radiobutton(settings, text='Второй', value=2)
rad3 = tk.Radiobutton(settings, text='Третий', value=3)
rad1.pack()
rad2.pack()
rad3.pack()


#rad2.grid(column=1, row=0)
#rad3.grid(column=2, row=0)




tk.Button(root, text="Quit",  background="#ff3333", foreground="#ccc", padx="16", pady="16", command=lambda root=root:quit(root)).pack(side = "right")

btn = tk.Button(text="Restart", background="#555", foreground="#ccc",
             padx="40", pady="16", command=click_button)
btn.pack(side = "right")


btn = tk.Button(text="Acceleration", background="#555", foreground="#ccc",
             padx="40", pady="16", command=acceleration_button)
btn.pack(side = "right")

btn = tk.Button(text="Change", background="#555", foreground="#ccc",
             padx="40", pady="16", command=change_gan)
btn.pack(side = "right")


def new_game(event=''):
    try:
        global Gan, screen1, balls, bullet, k_hard

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

        while ((count_T) or balls or 1):
            LB.update_board()



            if (len(Targets) == 0):
                click_button(1)


            count_T = 0;
            for t in Targets:
                count_T += t.live


            balls = cut(balls, 10)
            for b in balls:
                b.move()
                counter = 0
                for t in Targets:
                    #t.move()
                    if (b.hittest(t) and t.live):
                        k_hard *= k_hard
                        t.live = 0
                        t.hit()
                        LB.add_score("user24", (10/(t.r * math.sqrt(number_of_shorts))) * math.sqrt(t.vx*t.vx + t.vy*t.vy) / 50  )
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
    res_arr+=(str(L.name) + ',' + str(L.count)[0:5] + ";")
#mainloop()

set_users(res_arr)

#set_users(res_arr[:-1])
print(res_arr[:-1])

