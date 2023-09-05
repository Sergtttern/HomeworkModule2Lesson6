"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 2

Завдання 2: Інкапсуляція зі зміною значень через методи

Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
При спробі встановити недійсне значення, виведіть повідомлення про помилку.

(приклад у презентації)
"""

class Person:
    """
    клас "Person", який має властивості name (ім'я) і age (вік). Ці властивості є приватними,
    щоб вони не могли бути змінені напряму ззовні класу. Створені методи для доступу до цих властивостей
    та встановлення їх значень. Додані методи для зміни значень імені та віку.
    Зроблено так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
    При спробі встановити недійсне значення, виводить повідомлення про помилку.

    """

    def set_name(self, name):
        number_in_name = False
        for char in name:
            if char in "0123456789":
                print("Помилка: в імені не повинні міститися цифри")
                number_in_name = True
                break

        if not number_in_name:
            self.__name = name


    def set_age(self, age):
        if (age < 0) or (age > 120):
            print("Ви невірно ввели значення для віку")
        else:
            self.__age = age

    def get_name(self):
        if hasattr(self, '_Person__name'):
            return self.__name
        else:
            return "Імя відсутнє"

    def get_age(self):
        if hasattr(self, '_Person__age'):
            return self.__age
        else:
            return "Значення віку відсутнє"


person = Person()
person.set_name("John123")
person.set_age(150)
print(person.get_name())
print(person.get_age())
