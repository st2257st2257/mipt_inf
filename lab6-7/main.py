import pygame
from pygame.draw import *
from random import randint, uniform
pygame.init()


class User:
    """ Создаём класс пользователя и вызываем его методы при обработка фвйловых данных """
    def __init__(self, name="", score=0):
        self.name = name
        self.score = score

    def __add__(self, number):
        self.score += number

    def __del__(self):
        self.name = ""
        self.score = 0


class Ball:
    """
    Объект игры.
    При взаимодействии пользователя с программой вызываем методы шарика
    """
    def __init__(self, x, y, r=10, w=1, color=(50, 100, 150), vx=0, vy=0):
        # coord. of the ball
        self.x = x
        self.y = y
        # speed
        self.vx = vx
        self.vy = vy
        # other
        self.r = r  # radius
        self.w = w  # weight
        self.color = color  # color

    def move(self, h_max=100, h_min=0, w_max=100, w_min=0):
        """
        Вызываем функцию перемещения шарика при обновлении экрана
        Обрабатываем столкновения со стенами и случано изменяем скорость в заданном диапозоне
        :param h_max: максимальная высота экрана
        :param h_min: минимальная высота экрана
        :param w_max: максимальная ширина экрана
        :param w_min: минимальная ширина экрана
        :return:
        """
        if self.x < w_min:  # check speed and coord. params
            self.vx *= (-1.01)
            self.vy = uniform(-7, 7)
        if self.x > w_max:
            self.vx *= (-1.01)
            self.vy = uniform(-7, 7)
        if self.y < h_min:
            self.vy *= (-1.01)
            self.vx = uniform(-7, 7)
        if self.y > h_max:
            self.vy *= (-1.01)
            self.vx = uniform(-7, 7)

        # move ball
        self.x += self.vx
        self.y += self.vy

    def onclick(self, user, x, y):
        """
        Обрабатываем нажатие на экран:
        1) проверяем нажатие
        2) добавляем определённое количество очков
        :param user: пользователь
        :param x: Х коорд.
        :param y: У коорд.
        :return:
        """
        if ((self.x - x)**2 + (self.y - y)**2) < self.r*self.r:
            user.__add__(int(self.w*30/self.r))
            return 1
        else:
            return 0


# base setting
FPS = 5

screen_h_min = 0
screen_h_max = 300
screen_w_min = 0
screen_w_max = 500

screen = pygame.display.set_mode((screen_w_max, screen_h_max))

# color setting
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# files setting
data_file_name = "data.txt"

# user settings
users = []
U1 = User("U1", 0)
U2 = User("U2", 0)
users.append(U1)
users.append(U2)

# balls settings
balls = []
b1 = Ball(x=100, y=100, r=15, w=1, color=COLORS[0], vx=2,  vy=4)
b2 = Ball(x=200, y=150, r=10, w=1, color=COLORS[1],  vx=7, vy=1)
b3 = Ball(x=300, y=200, r=20, w=1, color=COLORS[2], vx=5,  vy=4)

bc1 = Ball(x=200, y=150, r=10, w=2, color=COLORS[3],  vx=-2, vy=3)
bc2 = Ball(x=100, y=100, r=5, w=2, color=COLORS[4], vx=2,  vy=-4)
bc3 = Ball(x=200, y=150, r=10, w=2, color=COLORS[5],  vx=-5, vy=7)

br1 = Ball(x=250, y=140, r=14, w=3, color=COLORS[1],  vx=4, vy=-3)
br2 = Ball(x=140, y=106, r=5, w=3, color=COLORS[3], vx=6,  vy=5)
br3 = Ball(x=220, y=150, r=10, w=3, color=COLORS[5],  vx=-8, vy=-1)

# adding balls to the main array
balls.append(b1)
balls.append(b2)
balls.append(b3)
balls.append(bc1)
balls.append(bc2)
balls.append(bc3)
balls.append(br1)
balls.append(br2)
balls.append(br3)


# base functions

# check click
def check(u0, x, y):
    for i in range(len(balls)):
        if balls[i].onclick(u0, x, y):
            del balls[i]
            return 1
    return 0


# read data
def get_users():
    gamers = open(data_file_name, 'r')
    data_p = gamers.read().split(';')
    gamers.close()
    return [data_p[i].split(',') for i in range(len(data_p))]


# write data
def set_users(ddata):
    gamers = open(data_file_name, 'w')
    res = ""
    for i in range(len(ddata)):
        res += str(ddata[i][0]) + "," + str(ddata[i][1]) + ';'
    gamers.write(res[:-1:])
    gamers.close()


# draw form
def draw(scr, b0):
    """
    Вместо того, чтобы создавать новые ненужные классы вводим
    тип объекта который рисуется на экране: так как программа не настолько
    большая, чтобы наследовать класс, это быудет оптимальным решением
    :param scr: поле на котором отображаем объекты
    :param b0: рисум шарик
    :return:
    """
    r = b0.r
    """Рисуем круг, треугольник и квадрат"""
    if b0.w == 1:
        circle(scr, b0.color, (b0.x, b0.y), b0.r)
    elif b0.w == 2:
        pygame.draw.polygon(scr, b0.color, [[int(b0.x - (r*3**(1/2)/2)), int(b0.y + r/2)], [int(b0.x), int(b0.y - r)],
                                            [int(b0.x + (r*3**(1/2)/2)), int(b0.y + r/2)]], int(r/2))
    elif b0.w == 3:
        pygame.draw.polygon(scr, b0.color,
                            [[int(b0.x - r / 2), int(b0.y - r/2)],
                             [int(b0.x - r / 2), int(b0.y + r/2)],
                             [int(b0.x + r / 2), int(b0.y + r/2)],
                             [int(b0.x + r / 2), int(b0.y - r/2)]], int(r/2))
    else:
        pass  # we can add sms. new: shape? type of the ball


def all_move():
    """Сразу передвигаем все шарики"""
    for i in range(len(balls)):
        balls[i].move(h_max=screen_h_max-50, h_min=screen_h_min+50, w_max=screen_w_max-50, w_min=screen_w_min+50)
        draw(screen, balls[i])


def update(u0):
    """Обрабатываем нажатия с клавиатуры"""
    for eevent in pygame.event.get():
        if eevent.type == pygame.QUIT:
            pass
        elif eevent.type == pygame.MOUSEBUTTONDOWN:
            print('Click! ', pygame.mouse.get_pos())
            check(u0=u0, x=pygame.mouse.get_pos()[0], y=pygame.mouse.get_pos()[1])


def main():
    """Настраиваем количество циклов и запускаем цикл отрисовки"""
    loops = 1000
    u = User("st2257", 0)
    for i in range(loops):
        update(u)


def if_in(vector, char):
    """Служебная функция: пользовательская версия index()"""
    for i in range(len(vector)):
        if char == vector[i]:
            return i+1
    return 0


def smart_sort(general_array, row):
    """Служебная функция: аналог sorted( arr, key )"""
    res = []
    for i in range(len(general_array)):
        max_v = sorted(row, key=lambda elem: elem)[len(row)-1]
        index = row.index(max_v)
        res.append(general_array[index])
        del row[index]
        del general_array[index]
    return res


"""Настраиваем основные параметры"""
pygame.display.update()
clock = pygame.time.Clock()
finished = False
data = get_users()
first_row = [data[0] for i in range(len(data))]
second_row = [data[int(1 * (i + 1) / (i + 1))] for i in range(len(data))]

print("data: ", data)

user_name = "user"
counter = 0
base_font = pygame.font.Font(None, 32)

# create lider table
liders_output = [pygame.font.Font(None, 32).render(data[i][0], 1, (255, 255, 255)) for i in range(min(5, len(data)))]
print("liders: ", liders_output)


U = User("st2257", 0)
while len(balls) != 0:
    """
    Рассматриваем разные этапы запуска программы:
    1) ввод имени
    2) проверка пользователя в базе данных
    3) основной цикл отрисовки
    """
    if counter == 0:
        """(1) ввод имени"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    """Обрабатываем удаление символа"""
                    user_name = user_name[:-1]
                elif event.key == pygame.K_RETURN:
                    """Обрабатываем момент нажатия пользователем на кнопку ввода"""
                    counter += 1
                else:
                    """Обрабатываем добавление символа в строку"""
                    user_name += event.unicode
        screen.fill((0, 0, 0))
        text_surface = base_font.render(user_name, 1, (255, 255, 255))
        general_text_surface = base_font.render("Enter name: ", 1, (255, 255, 255))

        screen.blit(text_surface, (250, 100))
        screen.blit(general_text_surface, (100, 100))

        pygame.display.flip()
        clock.tick(60)

    elif counter == 1:
        """(2) проверка пользователя в базе данных"""
        U.name = user_name
        # check user in our data
        if if_in(first_row, U.name):
            pass
        else:
            data.append([U.name, U.score])

        counter += 1
    else:
        """(3) основной цикл отрисовки"""
        screen.fill((0, 0, 0))

        t_s_s = base_font.render("name", 1, (255, 255, 255))
        t_s_n_s = base_font.render("score", 1, (255, 255, 255))

        screen.blit(t_s_s, (screen_w_max - 150, screen_h_min + 5))
        screen.blit(t_s_n_s, (screen_w_max - 70, screen_h_min + 5))

        for i in range(min(5, len(data))):
            t_s = base_font.render(str(data[i][0]), 1, (255, 255, 255))
            t_s_n = base_font.render(str(int(data[i][1])), 1, (255, 255, 255))

            screen.blit(t_s, (screen_w_max-140, screen_h_min+25+i*25))
            screen.blit(t_s_n, (screen_w_max - 50, screen_h_min + 25 + i * 25))

        clock.tick(FPS)
        update(U)
        all_move()
        pygame.display.update()
        screen.fill(BLACK)

        # update score
        f_row = [data[i][0] for i in range(len(data))]
        data[f_row.index(U.name)][1] = U.score
        print("Liders: ", [int(data[i][1]) for i in range(len(data))])
        data = smart_sort(data, [int(data[i][1]) for i in range(len(data))])


set_users(data)
print("enter value: ")
iii = int(input())
pygame.quit()
