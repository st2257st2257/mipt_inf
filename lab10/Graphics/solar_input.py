# coding: utf-8
# license: GPLv3

from solar_objects import Star


def read_space_objects_data_from_file(input_filename):
    """
    Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            print(line)
            if (object_type == "star") | (object_type == "Star"):
                star = parse_star_parameters(line)
                objects.append(star)
            if (object_type == "planet") | (object_type == "Planet"):
                planet = parse_planet_parameters(line)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line):
    """
    Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    line_array = line.split(" ")
    if line_array[0] == "Star":
        return Star(
            name=line_array[0], r=float(line_array[1]), color=line_array[2], m=float(line_array[3]),
            x=float(line_array[4]), y=float(line_array[5]),
            vx=float(line_array[6]), vy=float(line_array[7]))
    print("Unknown space object")


def parse_planet_parameters(line=""):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    line_array = line.split(" ")
    if line_array[0] == "Planet":
        return Star(name=line_array[0], r=float(line_array[1]), color=line_array[2], m=float(line_array[3]),
                    x=float(line_array[4]), y=float(line_array[5]),
                    vx=float(line_array[6]), vy=float(line_array[7]))


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    print(output_filename, space_objects)

    _file = open(output_filename, 'w')
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            _file.write(obj.type + " " + str(obj.R) + " " + obj.color + " " + str(obj.m) + " "
                        + str(obj.x) + " " + str(obj.y) + " "
                        + str(obj.Vx) + " " + str(obj.Vy) + "\n\n")

    print(out_file, "Wrote data")


if __name__ == "__main__":
    print("This module is not for direct call!")
