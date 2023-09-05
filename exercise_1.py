"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 1

Завдання 1: Проста інкапсуляція

Напишіть клас "Person", який має властивості name (ім'я) і age (вік). Зробіть ці властивості приватними,
щоб вони не могли бути змінені напряму ззовні класу. Забезпечте методи для доступу до цих властивостей
та встановлення їх значень.

(приклад у презентації)

"""

class Person:
    """
    клас "Person", який має властивості name (ім'я) і age (вік). Ці властивості є приватними,
    щоб вони не могли бути змінені напряму ззовні класу. Створені методи для доступу до цих властивостей
    та встановлення їх значень.
    """

    def set_name(self, name):
        self.__name = name#приватна властивість name

    def set_age(self, age):
        self.__age = age#приватна властивість age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person()
person.set_name("John")
person.set_age(25)
print(person.get_name())
print(person.get_age())
