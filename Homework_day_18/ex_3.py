"""Есть интернет-магазин.
Сейчас существуют три вида скидки:
● обычная — 5%;
● постоянный клиент — 10%;
● VIP — 20%.
Нужно реализовать расчёт скидки.
Главное условие
Код расчёта заказа не должен содержать конструкцию:
if discount_type == ...
для каждого нового типа скидки.
Добавьте возможность легко создать новую стратегию
скидки.
Усложнение
Добавьте:
● скидку на день рождения;
● скидку по промокоду.
При этом существующий код расчёта заказа менять не
должен.
Дедлайн: 04.09.2026"""

class SimplyDiscount:
    def calculate(self,price):
        return int(0.95 * price)

class PermanentDiscount:
    def calculate(self,price):
        return int(0.90 * price)
class VipDiscount:
    def calculate(self,price):
        return int(0.80 * price)

class BirthdayDiscount:
    def calculate(self, price):
        return int(0.15 * price)

PROMO_CODES = {
    "SALE":10,
    "BLACKFRIDAY":30
}
class PromocodeDiscount:
    def __init__(self,code):
        self.code = code
    def calculate(self,price):
        if self.code in PROMO_CODES:
            discount = PROMO_CODES[self.code]
            return int(price * discount/100)
        return 0

class Discount:
    def __init__(self,price_zakaz):
        self.price_zakaz = price_zakaz
    def discount_zakaz(self,price):
        return self.price_zakaz.calculate(price)

discount1 = Discount(SimplyDiscount())
print(discount1.discount_zakaz(100))

discount2 = Discount(BirthdayDiscount())
print(discount2.discount_zakaz(500))

discount3 = Discount(VipDiscount())
print(discount3.discount_zakaz(200))

discount4 = Discount(PermanentDiscount())
print(discount4.discount_zakaz(150))

discount5 = Discount(PromocodeDiscount("SALE"))
print(discount5.discount_zakaz(300))

