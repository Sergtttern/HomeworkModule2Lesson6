"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 7

Завдання 7: Використання super()

Розробіть клас "Square", який успадковує властивості і методи з класу "Rectangle".
Додайте властивість side_length (довжина сторони) і перевизначте методи, які використовують властивості width
і height класу "Rectangle", щоб вони використовували властивість side_length класу "Square".
Виведіть значення ширини, висоти і довжини сторони для об'єкта класу "Square".
(приклад є у презентації)

Приклад введення:

square = Square("Green", 8)
square.display_color() # Виведе "Color: Green"
print(square.width) # Виведе 8
print(square.height) # Виведе 8
print(square.side_length) # Виведе 8
"""


class Shape:
    """
    Базовий клас "Shape" (фігура), який має властивість color (колір) і метод display_color()
    для виведення коліру фігури.
    """
    def __init__(self, color):
        self._color = color

    def display_color(self):
        return self._color


class Rectangle(Shape):
    """
    Похідний клас "Rectangle" (прямокутник),
    який наслідує властивість color і додає властивості width (ширина) і height (висота).
    """
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def width_dislay(self):
        return self.width

    def height_dislay(self):
        return  self.height


class Square(Rectangle):
    """
    клас "Square", який успадковує властивості і методи з класу "Rectangle".
    Додана властивість side_length (довжина сторони) і перевизначені методи, які використовують властивості width
    і height класу "Rectangle", щоб вони використовували властивість side_length класу "Square".
    """
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def width_dislay(self):
        return self.side_length

    def height_dislay(self):
        return  self.side_length


square = Square("Green", 8)
square.display_color() # Виведе "Color: Green"
print(square.width_dislay()) # Виведе 8
print(square.height_dislay()) # Виведе 8
print(square.side_length) # Виведе 8
