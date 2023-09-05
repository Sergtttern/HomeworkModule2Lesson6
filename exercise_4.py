"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 4

Завдання 4: Просте наслідування

Створіть базовий клас "Shape" (фігура), який має властивість color (колір) і метод display_color()
для виведення коліру фігури. Створіть похідний клас "Rectangle" (прямокутник),
який наслідує властивість color і додає властивості width (ширина) і height (висота).
Забезпечте можливість встановлення значень ширини і висоти прямокутника та виведення їх значень.

(приклад у презентації)

shape = Shape("Red")
shape.display_color() # Виведе "Color: Red"

ООП - інкапсуляція, наслідування, поліморфізм, абстрактні методи. Приклади використання 19
rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color() # Виведе "Color: Blue"
print(rectangle.width) # Виведе 10
print(rectangle.height) # Виведе 5

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
    Забезпечена можливість встановлення значень ширини і висоти прямокутника та виведення їх значень.
    """
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def width_display(self):
        return self.width

    def height_display(self):
        return  self.height


shape = Shape("Red")
print(shape.display_color())

rectangle = Rectangle("Blue", 10, 5)
print(rectangle.display_color())
print(rectangle.width_display())
print(rectangle.height_display())
print(100*'*')
rectangle.set_width(100)
rectangle.set_height(100)
print(rectangle.width_display())
print(rectangle.height_display())
