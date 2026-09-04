"""Создайте класс Car, описывающий автомобиль.Реализуйте
приватные атрибуты для марки (__make), модели (__model) ипробега (__mileage).
Добавьте геттер и сеттер для пробега.
В сеттере проверьте условие: пробег не может быть
отрицательным числом, а также не может уменьшаться
(новый пробег должен быть больше или равен старому)."""

class Car:
    def __init__(self,make,model,mileage):
        self.__make = make
        self.__model = model
        self.__mileage = mileage

    @property
    def make (self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self,new_mileage):
        if new_mileage <0:
            raise  ValueError("Пробег не может быть отрицательным числом")
        if new_mileage < self.__mileage:
            raise ValueError("Пробег не может уменьшатся")
        self.__mileage = new_mileage
    def get_info(self):
        print(f"Автомобиль: {self.__make} , Марка: {self.__model} , Пробег: {self.__mileage} км")

car = Car("BMW","X6",30000)
car.get_info()
print()
car.mileage = 60000
car.get_info()
print()

try:
    car.mileage = 40000
except ValueError as e:
    print(e)