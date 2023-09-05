"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 3

Завдання 3: Комплексна інкапсуляція

Розробіть клас "Car", який містить такі властивості: make (марка автомобіля), model (модель автомобіля),
 year (рік випуску автомобіля) і mileage (пробіг автомобіля). Забезпечте можливість доступу до цих
 властивостей через методи, а також зробіть властивості "make" і "model" приватними.

Додайте метод "drive" до класу "Car", який збільшує пробіг автомобіля на задане значення. Перевірте,
чи не перевищує пробіг заданий ліміт (наприклад, 300 000 км), і виведіть повідомлення про досягнення ліміту
при спробі здійснити поїздку.

(приклад у презентації)
car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make()) # Виведе "Toyota"
print(car.get_model()) # Виведе "Camry"
print(car.get_year()) # Виведе 2020
print(car.get_mileage()) # Виведе 5000
car.drive(100) # Збільшення пробігу на 100
print(car.get_mileage()) # Виведе 5100
car.drive(300000) # Виведе повідомлення про досягнення ліміту

"""

class Car:
    """
    Клас "Car", який містить такі властивості: make (марка автомобіля), model (модель автомобіля),
    year (рік випуску автомобіля) і mileage (пробіг автомобіля). Забезпечено можливість доступу до цих
    властивостей через методи, а також реалізовані приватні властивості "make" і "model".
    """

    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.year

    def get_mileage(self):
        return self.mileage

    def drive(self, add_mileage):
        """
        метод який збільшує пробіг автомобіля на задане значення
        """
        if self.mileage + add_mileage > 300000:
            print("Перевищений ліміт для поїздки на цьому автомобілі")
        else:
            self.mileage = self.mileage + add_mileage

car = Car("Toyota", "Camry", 2020, 5000)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_mileage())
car.drive(100)
print(car.get_mileage())
car.drive(300000)
