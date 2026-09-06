"""Создайте класс Item, представляющий предмет в инвентаре
персонажа.
Каждый предмет имеет:
● name — название;
● weight — вес;
● price — стоимость.
Необходимо перегрузить операторы:
● + — объединяет два предмета в «набор» и возвращает
их общую стоимость;
● < — сравнивает предметы по весу;
● == — считает предметы одинаковыми, если совпадают
их названия;
● str() — выводит предмет в удобном формате."""


class Item:
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.price = price
    def __add__(self, other):
        if isinstance(other,Item):
            return self.price + other.price
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other,Item):
            return self.weight < other.weight
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other,Item):
            return self.name == other.name
        return NotImplemented
    def __str__(self):
        return f"Название:{self.name}, Вес:{self.weight}, Стоимость:{self.price} "

sword_1 = Item("Огненный меч", 5, 350)
blade = Item("Разрушительный клинок" , 3, 190)
sword_2 = Item("Огненный меч", 8,500)

print("Инвентарь персонажа:")
print(sword_1)
print(blade)
print(sword_2)
print( 25 * "-")

print(f"Общая стоимость sword_1 и blade = {sword_1 + blade}")
print(f"Общая стоимость sword_1 и sword_2 = {sword_1 + sword_2}")
print( 25 * "-")

print(f"sword_2 легче sword_1: {sword_2 < sword_1}")
print(f"blade легче sword_2: {blade < sword_2}")
print( 25 * "-")

print(f"sword_1 и sword_2 одинаковые предметы: {sword_1 == sword_2}")
print(f"sword_1 и blade одинаковы предметы: {sword_1 == blade}")
