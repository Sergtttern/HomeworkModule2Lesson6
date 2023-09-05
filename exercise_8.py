"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 8

Завдання 8: Автосалон

Опис: Ви розробляєте програму для автосалону, яка обробляє інформацію про
різні автомобілі. У вас є базовий абстрактний клас Car (автомобіль), який містить
загальну інформацію про автомобіль, таку як марка та модель. У додаткових
класах, які успадковують від Car , ви розширюєте функціональність для конкретних
типів автомобілів.
1. Клас Sedan (седан) успадковує від Car . Він має додатковий атрибут - кількість
дверей.
2. Клас SUV успадковує від Car . Він має додатковий атрибут - кількість
пасажирських місць.
3. Клас SportsCar (спортивний автомобіль) успадковує від Car . Він має
додатковий атрибут - максимальна швидкість.
Завдання: Створіть об'єкти різних класів (седан, позашляховик, спортивний
автомобіль) і використовуйте їх функціонал. Виведіть інформацію про кожен
автомобіль, включаючи загальну інформацію з Car та специфічну інформацію для
кожного класу.
Приклад використання:

# Створюємо об'єкти різних класів
sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)
# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()

Очікуваний вивід:

ООП - інкапсуляція, наслідування, поліморфізм, абстрактні методи. Приклади використання 22
Car: Toyota Camry
Doors: 4
-------------------------
Car: Ford Explorer
Seats: 7
-------------------------
Car: Ferrari 488 GTB
Max Speed: 330 km/h

"""
from abc import abstractmethod

class Car:
    """
    базовий абстрактний клас Car (автомобіль), який містить
    загальну інформацію про автомобіль, таку як марка та модель.
    """
    @abstractmethod
    def __init__(self, car_brand, car_model):
        self.car_brand = car_brand
        self.car_model = car_model

    @abstractmethod
    def display_info(self):
        print(f"Car: {self.car_brand}\nModel: {self.car_model}")

class Sedan(Car):
    """
    Клас Sedan (седан) успадковує від Car . Він має додатковий атрибут - кількість
    дверей.
    """
    def __init__(self, car_brand, car_model, car_doors_number):
        super().__init__(car_brand, car_model)
        self.car_doors_number = car_doors_number

    def display_info(self):
        print(f"Car: {self.car_brand} {self.car_model}\nDoors: {self.car_doors_number}")

class SUV(Car):
    """
    Клас SUV успадковує від Car . Він має додатковий атрибут - кількість
    пасажирських місць.
    """
    def __init__(self, car_brand, car_model, car_passenger_seats_number):
        super().__init__(car_brand, car_model)
        self.car_passenger_seats_number = car_passenger_seats_number

    def display_info(self):
        print(f"Car: {self.car_brand} {self.car_model}\nSeats: {self.car_passenger_seats_number}")

class SportsCar(Car):
    """
    Клас SportsCar (спортивний автомобіль) успадковує від Car . Він має
    додатковий атрибут - максимальна швидкість.
    """
    def __init__(self, car_brand, car_model, car_max_speed):
        super().__init__(car_brand, car_model)
        self.car_max_speed = car_max_speed

    def display_info(self):
        print(f"Car: {self.car_brand} {self.car_model}\nMax Speed: {self.car_max_speed}")

sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)
# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()
