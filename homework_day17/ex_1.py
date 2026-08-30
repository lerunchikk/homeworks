"""Базовый класс Order. У заказа должны быть:
● номер;
● сумма;
● статус.
Реализуйте методы:
● pay()
● cancel()
Заказ нельзя отменить после оплаты. Если пользователь
пытается выполнить недопустимую операцию, должно
возникать собственное исключение: InvalidOrderStateError.
Создайте иерархию:
OrderError
└── InvalidOrderStateError
● Добавьте __str__: Объект заказа должен красиво
отображаться: Заказ #1001: 250 EUR, статус: оплачено
● Добавьте __eq__:Два заказа считаются одинаковыми,
если у них одинаковый номер"""

class OrderError(Exception):
    pass

class InvalidOrderStateError(OrderError):
    pass

class Order:
    def __init__(self, number, summa, currency='EUR'):
        self.number = number
        self.summa = summa
        self.currency = currency
        self.status = "не оплачено"

    def pay(self):
        if self.status == "оплачено":
            raise InvalidOrderStateError(f"Заказ №{self.number} уже оплачен")
        if self.status == "отменено":
            raise InvalidOrderStateError(f"Нельзя оплатить отмененный заказ №{self.number}")
        self.status = "оплачено"

    def cancel(self):
        if self.status == "оплачено":
            raise InvalidOrderStateError(f"Заказ №{self.number} нельзя отменить после оплаты")
        if self.status == "отменено":
            raise InvalidOrderStateError(f"Заказ №{self.number} уже отменен")
        self.status = "отменено"

    def __str__(self):
        return f"Заказ #{self.number}: {self.summa} {self.currency}, статус: {self.status}"

    def __eq__(self, other):
        if isinstance(other, Order):
            return self.number == other.number
        return NotImplemented

order1 = Order(1001, 250)
print(order1)

order1.pay()
print(order1)

order2 = Order(1001, 500, "USD")
order3 = Order(1002,250)
print(f"order1 == order2: {order1 == order2}")
print(f"order1 == order3: {order1 == order3}")

try:
    order1.cancel()
except InvalidOrderStateError as e:
    print(f"Ошибка: {e}")

try:
    order1.pay()
except InvalidOrderStateError as e:
    print(f"Ошибка оплаты: {e}")