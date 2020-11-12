# coding: utf-8
# license: GPLv3
# from solar_objects import Dot

"""
    Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
    При отрисовке графика:
1) будем хранить только текующие элементы
2) будем масштабировать график по осям так чтобы по каждой
он занимал 100%
это поможет более наглядному отображению графика
3) будем содержать легенду графика в переменной description
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр.
"""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.4*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """
    Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """
    Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """

    return -int(y*scale_factor) + window_height//2  # FIXME: not done yet


def create_star_image(space, star):
    """
    Создаёт отображаемый объект звезды.

    Параметры:

    **space** — холст для рисования.
    **star** — объект звезды.
    """

    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """
    Создаёт отображаемый объект планеты.

    Параметры:

    **space** — холст для рисования.
    **planet** — объект планеты.
    """
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_system_name(space, system_name):
    """
    Создаёт на холсте текст с названием системы небесных тел.
    Если текст уже был, обновляет его содержание.

    Параметры:

    **space** — холст для рисования.
    **system_name** — название системы тел.
    """
    space.create_text(30, 80, tag="header", text=system_name, font=header_font)


def update_object_position(space, body):
    """
    Перемещает отображаемый объект на холсте.

    Параметры:

    **space** — холст для рисования.
    **body** — тело, которое нужно переместить.
    """
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2*r, window_height + 2*r)  # положить за пределы окна
    else:
        space.coords(body.image, x - r, y - r, x + r, y + r)

    """Для зелёной планеты (Земли) обновляем графики"""
    if (body.type == "Planet") & (body.color == "green"):
        update_graphic(space, body.graphic_r_t)
        update_graphic(space, body.graphic_v_t)
        update_graphic(space, body.graphic_v_r)


def create_lines(space, graphic):
    """
    Удаляем линии с холста и создаём новые.
    Отображаем побочные элементы графика
    """
    min_x = graphic.min_x
    max_x = graphic.max_x
    min_y = graphic.min_y
    max_y = graphic.max_y
    x_bias = graphic.x_bias
    y_bias = graphic.y_bias

    """Обнуляем массив линий, так как при каждой отрисовке происходит его пополнение"""
    for i in range(len(graphic.id_lines_array)):
        space.delete(graphic.id_lines_array[i])
    for i in range(len(graphic.border_array)):
        space.delete(graphic.border_array[i])
    graphic.id_lines_array = []
    graphic.border_array = []

    """Перерисовываем линии графика"""
    for i, dot in enumerate(graphic.dots_array[:-1]):
        graphic.id_lines_array.append(space.create_line(
            x_bias + (dot.x - min_x) * graphic.width / (max_x - min_x),                      # x1
            y_bias + graphic.height - (dot.y - min_y) * graphic.height / (0.1 + max_y - min_y),                     # y1
            x_bias + (graphic.dots_array[i+1].x - min_x) * graphic.width / (max_x - min_x),  # x2
            y_bias + graphic.height - (graphic.dots_array[i+1].y - min_y) * graphic.height / (0.1 + max_y - min_y),  # y
            fill=graphic.color
        ))

    """Устанавливаем граныцы графика"""
    """Верхняя линия"""
    graphic.border_array.append(space.create_line(
            x_bias,
            y_bias,
            x_bias + graphic.width,
            y_bias,
            fill="white"))

    """Правая линия"""
    graphic.border_array.append(space.create_line(
            x_bias + graphic.width,
            y_bias,
            x_bias + graphic.width,
            y_bias + graphic.height,
            fill="white"))

    """Нижняя линия"""
    graphic.border_array.append(space.create_line(
            x_bias + graphic.width,
            y_bias + graphic.height,
            x_bias,
            y_bias + graphic.height,
            fill="white"))

    """Левая линия"""
    graphic.border_array.append(space.create_line(
            x_bias,
            y_bias + graphic.height,
            x_bias,
            y_bias,
            fill="white"))

    """Рисуем оси координат для более удобного отображения"""
    graphic.border_array.append(space.create_line(
            x_bias + graphic.width / 2,
            y_bias,
            x_bias + graphic.width / 2,
            y_bias + graphic.height,
            fill="white"))

    graphic.border_array.append(space.create_line(
            x_bias,
            y_bias + graphic.height / 2,
            x_bias + graphic.width,
            y_bias + graphic.height / 2,
            fill="white"))

    """Выводим описание грфика"""
    graphic.border_array.append(space.create_text(
        x_bias + 6 + len(graphic.description)*2,
        y_bias + graphic.height + 8,
        text=graphic.description,
        font="Verdana 10",
        fill=graphic.color
    ))


def update_graphic(space, graphic):
    """
    Обновляем отображенный график:
    Удалякем с холста старые линии и дорисавываем новые
    """
    graphic.update(1)
    for dot in graphic.id_lines_array:
        space.delete(dot)

    create_lines(space, graphic)


if __name__ == "__main__":
    print("This module is not for  direct call!")
