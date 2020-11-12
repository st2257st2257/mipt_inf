# coding: utf-8
# license: GPLv3
from math import sin, cos, tan


class Dot:
    """Приработе с массивами в питоне возникают проблемы. Потому создадим новый класс"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.arr = [x, y]

    def print(self):
        print(self.x, self.y, self.arr)


class Graphic:
    def __init__(self, formula="0", x0=sin(tan(cos(1))),
                 x_bias=100, y_bias=100,
                 t=100,
                 color="white",
                 description="",
                 height=100,
                 width=100,
                 show_type="time"):
        """Устанавливаем основные параметры графика"""

        self.formula = formula
        """Формула по которой расчитываем график"""

        self.dots_array = []
        """Массив точе для построения графика"""

        self.id_lines_array = []
        """Массив линий, из которых состоит график"""

        self.border_array = []
        """Объекты, отвечающие за формление графика"""

        self.x0 = x0
        """Начальное значение аргумента"""

        self.height = height
        """Выстота графика"""

        self.width = width
        """Ширина графика"""

        self.x_bias = x_bias
        """Смешение по оси ОХ"""

        self.y_bias = y_bias
        """Смещение по оси ОУ"""

        self.T = t
        """Количество точек, выводимых на графике"""

        self.color = color
        """"""

        self.description = description
        """Описание графика"""

        self.show_type = show_type      # time - depend only on time: arr - depend only on array
        """Тип отображения графика"""

        counter = 0
        for x in range(self.T):
            try:
                self.dots_array.append(Dot(x, eval(self.formula)))
                counter += 1
            except 1:
                print("Error: division by zero")

        """Настраиваем основные параметры для дальнейшей работы системы"""
        arr_y = sorted(self.dots_array, key=lambda dot: dot.y)

        self.max_y = arr_y[len(arr_y)-1]
        self.min_y = arr_y[0]

        self.max_x = self.x0 + counter
        self.min_x = self.x0

    def update(self, dx=1):
        """Обновляем параметры графика при перерисовке.
        Дополнительное обновление, связанное с отображением графика на холсте,
        прописано в файле solar.ru.
        Рассматриваем два случая отображения графика:
        1) зависит только от времени
        2) зависит только от массива
        Первый нужен дл я отображения графика по формуле, второй для отображения графика
        из массива значений
        """

        if self.show_type == "time":
            """(1) зависит только от времени"""
            self.x0 += dx
            x0 = self.x0
            self.dots_array = []

            counter = 0
            for x in range(self.T):
                try:
                    self.dots_array.append(Dot(x+x0, eval(self.formula)))
                    counter += 1
                except 1:
                    print("Error: division by zero")

            """Настраиваем основные параметры для дальнейшей работы системы"""
            arr_y = sorted(self.dots_array, key=lambda dot: dot.y)

            self.max_y = arr_y[len(arr_y) - 1].y
            self.min_y = arr_y[0].y

            self.max_x = self.x0 + counter
            self.min_x = self.x0

        elif self.show_type == "arr":
            """(2) зависит только от массива точек"""
            self.dots_array = self.dots_array[max(0, len(self.dots_array) - self.T)::]

            arr_x = sorted(self.dots_array, key=lambda dot: dot.x)
            arr_y = sorted(self.dots_array, key=lambda dot: dot.y)

            self.max_y = arr_y[len(arr_y) - 1].y
            self.min_y = arr_y[0].y

            self.max_x = arr_x[len(arr_x) - 1].x
            self.min_x = arr_x[0].x

            self.x0 = self.min_x

    def __del__(self):
        self.dots_array = []


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "Star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""

    graphic_v_t = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: v(t)",
                          x_bias=50, y_bias=250)
    """График для зависимости модуля скорости от времени"""

    graphic_r_t = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: r(t)",
                          x_bias=50, y_bias=400)
    """График для зависимости радиуса от времени"""

    graphic_v_r = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: v(r)",
                          x_bias=50, y_bias=550)
    """График для зависимости модуля скорости от радиуса"""

    def __init__(self, name="Star", m=1, x=100, y=100, vx=0, vy=0, fx=0, fy=0, r=1,
                 color="red", image=None):
        """Делаем функцию, которя записывает принятые параметры в наши переменные"""
        self.type = name
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.Fx = fx
        self.Fy = fy
        self.R = r
        self.color = color
        self.m = m
        self.image = image


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "Planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    R_to_star = 0
    """Растояние от планеты до солнца"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""

    graphic_v_t = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: v(t)",
                          x_bias=50, y_bias=250)
    """График для зависимости модуля скорости от времени"""

    graphic_r_t = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: r(t)",
                          x_bias=50, y_bias=400)
    """График для зависимости радиуса от времени"""

    graphic_v_r = Graphic(show_type="arr",
                          color="white",
                          description="GRAPH: v(r)",
                          x_bias=50, y_bias=550)
    """График для зависимости модуля скорости от радиуса"""

    def __init__(self, name="Planet", m=1, x=100, y=100, vx=0, vy=0, fx=0, fy=0, r=1,
                 color="blue", image=None):
        """
        Делаем функцию, которя записывает принятые параметры в наши переменные.
        Описания переменных написаны ранее
        """
        self.type = name
        self.x = x
        self.y = y
        self.Vx = vx
        self.Vy = vy
        self.Fx = fx
        self.Fy = fy
        self.R = r
        self.color = color
        self.m = m
        self.image = image

    def __add__(self, dot, g_type="v_t"):
        """
        Делаем одну функцию для добваления точки в график,
        и как аргумент принимаем тип графика. Это помогает
        избавиться от разных функций
        """
        if g_type == "v_t":
            self.graphic_v_t.dots_array.append(dot)
        elif g_type == "v_r":
            self.graphic_v_r.dots_array.append(dot)
        elif g_type == "r_t":
            self.graphic_r_t.dots_array.append(dot)
            self.graphic_r_t.update()
        print("New dot added to" + g_type)
