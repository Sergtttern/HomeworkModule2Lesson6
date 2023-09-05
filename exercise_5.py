"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 5

Завдання 5: Перевизначення методів

Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color().
В методі display_color() виведіть повідомлення про колір прямокутника і додайте також виведення
повідомлення про його розміри (ширину і висоту).

(приклад у презентації)

Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод
display_color(). В методі display_color() виведіть повідомлення про колір
прямокутника і додайте також виведення повідомлення про його розміри (ширину і
висоту).
Приклад введення:

rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color() # Виведе "Color: Blue, Width: 10, Height: 5"
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
    Перевизначений метод display_color().
    В методі display_color() виводиться повідомлення про колір прямокутника і повідомлення про
    його розміри (ширину і висоту).
    """
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def display_color(self):
        """
        метод display_color() виведить повідомлення про колір прямокутника і додано також виведення
        повідомлення про його розміри (ширину і висоту).
                """
        return f"Color: {self._color}, Width: {self.width}, Height: {self.height}"

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
