"""
Модуль 2 Python Advanced, Урок №6. ООП, Вправа 6

Завдання 6: Багатоуровневе наслідування

Завдання та приклад дивиться у презентації

Завдання 3: Багатоуровневе наслідування
Опис: Ви розробляєте програму для інформації про тварин в зоопарку. У вас є
базовий клас Animal (тварина), який містить загальну інформацію про тварину, таку
як назва та вид. У додаткових класах, які успадковують від Animal , ви розширюєте
функціональність для конкретних видів тварин.
1. Клас Mammal (ссавець) успадковує від Animal . Він має додатковий атрибут - тип
харчування (наприклад, травоїдний, всеїдний, хижий).
2. Клас Carnivore (хижак) успадковує від Mammal . Він має додатковий атрибут -
кількість зубів.
3. Клас Lion (лев) успадковує від Carnivore . Він має додатковий атрибут - розмір
гриви.
Завдання: Створіть об'єкти різних класів (лев, хижак, ссавець) і використовуйте їх
функціонал. Виведіть інформацію про кожну тварину, включаючи загальну
інформацію з Animal та специфічну інформацію для кожного класу.
Приклад використання:

ООП - інкапсуляція, наслідування, поліморфізм, абстрактні методи. Приклади використання 20
# Створюємо об'єкти різних класів
lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")
# Виводимо інформацію про кожну тварину
lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()

Очікуваний вивід:

Animal: Simba
Species: Lion
Diet Type: Carnivore
Teeth Count: 30
Mane Size: Large
-------------------------
Animal: Tiger
Species: Carnivore
Diet Type: Carnivore
Teeth Count: 40
-------------------------
Animal: Elephant
Species: Mammal
Diet Type: Herbivore
"""


class Animal:
    """
    базовий клас Animal (тварина), який містить загальну інформацію про тварину, таку
    як назва та вид.
    """
    def __init__(self, animal, specie):
        self.animal = animal
        self.specie = specie

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecie: {self.specie}")


class Mammal(Animal):
    """
    Клас Mammal (ссавець) успадковує від Animal . Він має додатковий атрибут - тип
    харчування (наприклад, травоїдний, всеїдний, хижий).
    """
    def __init__(self, name, specie, nutrition):
        super().__init__(name, specie)
        self.nutrition = nutrition

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecie: {self.specie}\nNutrition: {self.nutrition}")

class Carnivore(Mammal):
    """
    Клас Carnivore (хижак) успадковує від Mammal . Він має додатковий атрибут -
    кількість зубів.
    """
    def __init__(self, name, specie, nutrition, tooth_number):
        super().__init__(name, specie, nutrition)
        self.tooth_number = tooth_number

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecie: {self.specie}\nNutrition: {self.nutrition}\n"
              f"Teeth Count: {self.tooth_number}")


class Lion(Carnivore):
    """
    Клас Lion (лев) успадковує від Carnivore . Він має додатковий атрибут - розмір
    гриви.
    """
    def __init__(self, name, specie, nutrition, tooth_number, mane_size):
        super().__init__(name, specie, nutrition, tooth_number)
        self.mane_size = mane_size

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecie: {self.specie}\nNutrition: {self.nutrition}\n"
              f"Teeth Count: {self.tooth_number}\nMane Size: {self.mane_size}")


lion = Lion("Lion", "Mammal", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Mammal", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()
