class Figure:
    sides_count = 0

    def __init__(self, color, *sides: int):
        if self.__is_valid_color(*color):
            self.__color = color
            self.filled = True # фигура закрашена
        else:
            self.__color = [0, 0, 0] # фигура не закрашена
            self.filled = False

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count


    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        self.filled = True
        return self.__color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides):
            return True
        else:
            return False


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__len__() / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        s = self.__len__()/2
        return (s * ((s - sides[0]) * (s - sides[1]) * (s - sides[2]))) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        else:
            sides = [1] * self.sides_count

        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3





circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.filled)
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# -------Доп. проверка--------
# triangle1  = Triangle((20, 15, 40), 3, 7, 8)
# print(triangle1.get_sides())
# print(triangle1.filled) # цвета соответствуют, фигура закрашена (True)
#
# triangle2 = Triangle((270, 15, 40), 3, 7, 8)
# print(triangle2.filled) # цвета не соответствуют (270>255), фигура не закрашена (False)
#
#
# triangle1.set_color(53, 25, 42)
# print(triangle1.get_color())
#
# cube2 = Cube((222, 35, 130), 6, 2)
# print(cube2.get_sides())  # выводит [1, 1, 1, ..... 1] (12), т.к. задано больше одного значения
# print(triangle1.get_square())







