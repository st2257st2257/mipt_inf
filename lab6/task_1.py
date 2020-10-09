import pygame
from pygame.draw import *
from random import randint
pygame.init()


class user:
    def __init__(self, name="", score=0):
        self.name = name;
        self.score = score;

    def __add__(self, number):
        self.score += number;

    def __del__(self):
        self.name = "";
        self.score = 0;


class ball:
    def __init__(self, x, y, r=10, w=1, color = (50,100,150), vx=0, vy=0):
        # coord. of the ball
        self.x = x;
        self.y = y;
        # speed
        self.vx = vx;
        self.vy = vy;
        # other
        self.r = r;  # radius
        self.w = w;  # weight
        self.color = color; # color

    def __del__(self):
        self.x = self.y = self.vx = self.vy = self.r = 0; #delete all

    def move(self,h_max=100,h_min=0,w_max=100,w_min=0):
        if (self.x < w_min): #check speed and coord. params
            self.vx *= (-1.1)
        if (self.x > w_max):
            self.vx *= (-1.1)

        if (self.y < h_min):
            self.vy *= (-1.1)
        if (self.y > h_max):
            self.vy *= (-1.1)

        #move ball
        self.x += self.vx; self.y += self.vy;

    def onclick(self, user,x,y):
        if (((self.x - x)**2 + (self.y - y)**2) < self.r*self.r):
            user.__add__(int(self.w*30/self.r));
            self.__del__();
            return 1;
        else:
            return 0;




#base setting
FPS = 5

screen_h_min = 0; screen_h_max = 300;
screen_w_min = 0; screen_w_max = 500;

screen = pygame.display.set_mode((screen_w_max, screen_h_max))

#color setting
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#files setting

#user settings
users = []
U1 = user("U1", 0);
U2 = user("U2", 0);
users.append(U1); users.append(U2);

#balls settings
balls = []
b1 = ball(x=100, y=100, r=15, w=1, color = COLORS[0], vx = 2,  vy = 4);
b2 = ball(x=200, y=150, r=10, w=1, color = COLORS[1],  vx = 7, vy = 1);
b3 = ball(x=300, y=200, r=20, w=1, color = COLORS[2], vx = 5,  vy = 4);

bc1 = ball(x=200, y=150, r=10, w=1, color = COLORS[3],  vx = -2, vy = 3);
bc2 = ball(x=100, y=100, r=5, w=1, color = COLORS[4], vx = 2,  vy = -4);
bc3 = ball(x=200, y=150, r=10, w=1, color = COLORS[5],  vx = -5, vy = 7);

#b3 = ball(x=randint(screen_h_min+100, screen_h_max-100), y=randint(screen_w_min+100, screen_w_max-100), r=randint(10,15), w=1, color = COLORS[randint(0,5)], vx = randint(0,5),  vy = randint(0,5));

balls.append(b1); balls.append(b2); balls.append(b3);
balls.append(bc1); balls.append(bc2); balls.append(bc3);





#base functions

#check click
def check(u0,x,y):
    for i in range(len(balls)):
        if (balls[i].onclick(u0,x,y)):
            del balls[i]
            return 1;
    return 0;

#read data
def get_users():
    gamers = open("data.txt", 'r')
    Data_p = gamers.read()[0:-1:].split(';')
    Data = [Data_p[i].split(',')  for i in range(len(Data_p))]
    gamers.close()
    return Data

#write data
def set_users(Data):
    gamers = open("data.txt", 'w')
    res = ""
    for i in range(len(Data)):
        res += str(Data[i][0]) + "," + str(Data[i][1]) + ';'
    gamers.write(res[:-1:])
    gamers.close()

#draw form
def draw(scr, b0):
    if (b0.w == 1):
        circle(scr, b0.color, (b0.x, b0.y), b0.r)

    elif (b0.w == 2):
        pass
    elif (b0.w == 3):
        pass

    else:
        pass
def all_move():
    for i in range(len(balls)):
        balls[i].move(h_max = screen_h_max-50, h_min = screen_h_min+50, w_max = screen_w_max-50, w_min = screen_w_min+50)
        draw(screen, balls[i])


def update(u0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!', pygame.mouse.get_pos())
            check(u0 = u0,x = pygame.mouse.get_pos()[0],y = pygame.mouse.get_pos()[1])

def main():
    loops = 1000;
    User = user("st2257",0);
    for i in range(loops):
        update(User);

def if_in(vector, char):
    for i in range(len(vector)):
        if char == vector[i]:
            return (i+1)
    return 0

def array_max(row):
    m = 0;
    for i in range(len(row)):
        if(row[i] >= m):
            m = row[i]
    return m

def smart_sort(general_array, row):
    res = []
    print(row, general_array)
    for i in range(len(general_array)):
        max_v = array_max(row)
        index = row.index(max_v)
        print(index)
        res.append(general_array[index])
        del row[index]
        del general_array[index]

        print(row,general_array)
    print(res)
    return res

'''
def new_ball():
    рисует новый шарик 
    global x,y,r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

'''


pygame.display.update()
clock = pygame.time.Clock()
finished = False
data = get_users()
first_row = [data[0] for i in range(len(data))]
second_row = [data[1] for i in range(len(data))]
print("date: ", data)







user_name = "user"
counter = 0
base_font = pygame.font.Font(None,32)

#create lider table
liders_output = [pygame.font.Font(None,32).render(data[i][0],1,(255,255,255)) for i in range(min(5,len(data)))]
print("liders: ", liders_output)



User = user("st2257", 0)
while len(balls)!=0:
    if counter==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]

                elif event.key == pygame.K_RETURN:  #RETURN
                    counter+=1;
                else:
                    user_name += event.unicode
        screen.fill((0,0,0))
        text_surface = base_font.render(user_name,1,(255,255,255))
        general_text_surface = base_font.render("Enter name: ", 1, (255, 255, 255))

        screen.blit(text_surface, (250, 100))
        screen.blit(general_text_surface,(100,100))

        pygame.display.flip()
        clock.tick(60)

    elif counter == 1:
        User.name = user_name
        # check user in our data
        if (if_in(first_row, User.name)):
            pass
        else:
            data.append([User.name, User.score])

        counter+=1;
    else:
        screen.fill((0, 0, 0))

        t_s_s = base_font.render("name", 1, (255, 255, 255))
        t_s_n_s = base_font.render("score", 1, (255, 255, 255))

        screen.blit(t_s_s, (screen_w_max - 150, screen_h_min + 5))
        screen.blit(t_s_n_s, (screen_w_max - 70, screen_h_min + 5))

        for i in range(min(5,len(data))):
            t_s = base_font.render(str(data[i][0]),1,(255,255,255))
            t_s_n = base_font.render(str(int(data[i][1])), 1, (255, 255, 255))

            screen.blit( t_s , (screen_w_max-140, screen_h_min+25+i*25))
            screen.blit(t_s_n, (screen_w_max - 50, screen_h_min + 25 + i * 25))

        clock.tick(FPS)
        update(User)
        all_move()
        pygame.display.update()
        screen.fill(BLACK)

        #update score
        f_row = [data[i][0] for i in range(len(data))]
        data[f_row.index(User.name)][1] = User.score
        print([int(data[i][1]) for i in range(len(data))])
        data = smart_sort(data, [int(data[i][1]) for i in range(len(data))] )
        ##first_row = [data[0] for i in range(len(data))]
        ##second_row = [data[1] for i in range(len(data))]

set_users(data)
ptin("enter value: ")
iii = int(input())
pygame.quit()
