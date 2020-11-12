# coding: utf-8
# license: GPLv3

import math
from solar_objects import *
gravitational_constant = 6.67408E-11
time_boost = 86400
"""Гравитационная постоянная Ньютона G"""


def update_an(object_class, space_object):
    """
    Рассматриваем все случаи взаимного расположения тел и считаем радиус-вектор
    одного относительно другого
    """
    pi = 3.14
    an = 0
    if ((space_object.x - object_class.x) > 0) & ((space_object.y - object_class.y) > 0):
        an = abs(math.atan((space_object.y - object_class.y) / (space_object.x - object_class.x)))
    elif ((space_object.x - object_class.x) < 0) & ((space_object.y - object_class.y) > 0):
        an = pi - abs(math.atan((space_object.y - object_class.y) / (space_object.x - object_class.x)))
    elif ((space_object.x - object_class.x) < 0) & ((space_object.y - object_class.y) < 0):
        an = -pi + abs(math.atan((space_object.y - object_class.y) / (space_object.x - object_class.x)))
    elif ((space_object.x - object_class.x) > 0) & ((space_object.y - object_class.y) < 0):
        an = -abs(math.atan((space_object.y - object_class.y) / (space_object.x - object_class.x)))
    an *= -1
    return an


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = 0
    body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = math.sqrt((body.x - obj.x)**2 + (body.y - obj.y)**2)
        v = math.sqrt(body.Vx**2 + body.Vy**2)

        """Находим растояние до звезды и записываем его в массив точек графика r(t)"""
        if (obj.type == "Star") & (body.type != "Star") & (body.color == "green"):
            body.R_to_star = r
            """добавляем в графики планеты точки"""
            body.graphic_r_t.dots_array.append(Dot(body.graphic_r_t.max_x+1, r / 1000000))
            body.graphic_v_t.dots_array.append(Dot(body.graphic_r_t.max_x + 1, v / 1000))
            body.graphic_v_r.dots_array.append(Dot(r / 1000000000, v / 1000))

        """В соответствии с углом считаем силу"""
        angle = update_an(body, obj)
        body.Fx += abs(gravitational_constant * body.m * obj.m/(r**2)) * math.cos(angle)
        body.Fy -= abs(gravitational_constant * body.m * obj.m/(r**2)) * math.sin(angle)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    dt *= 1

    """Из второго закона Ньютона и закона движения находим новые параметры объекта"""
    ax = body.Fx / body.m
    ay = body.Fy / body.m

    body.Vx += ax * (dt * time_boost)
    body.Vy += ay * (dt * time_boost)

    body.x += body.Vx * (dt * time_boost)
    body.y += body.Vy * (dt * time_boost)


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
