"""
Создайте класс BankAccount, который представляет
банковский счёт. У объекта должны быть:
owner — имя владельца; _balance — текущий баланс.
Реализуйте методы:
● deposit(amount) — пополнение счёта;
● withdraw(amount) — снятие денег;
● get_balance() — получение текущего баланса.
Правила:
● нельзя пополнить счёт на отрицательную или нулевую
сумму;
● нельзя снять отрицательную или нулевую сумму;
● нельзя снять больше денег, чем есть на счёте.
Замените get_balance() на property, чтобы баланс можно
было получать так:
"""
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    def deposit(self,amount):
        if amount <=0:
            raise ValueError("Сумма пополнения счета должна быть больше нуля")
        self._balance +=amount
        print(f"Баланс пополнен на {amount} руб.")

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Невозможно снять деньги , если на балансе 0")
        if amount>self._balance:
            raise ValueError("Нельзя снять больше денег, чем есть на счете")
        self._balance -=amount
        print(f"С баланса списано: {amount} руб.")

    @property
    def balance(self):
        return self._balance

account = BankAccount("Ваня",230)
print( f"Владелец: {account.owner}, Текущий баланс: {account.balance} руб.")
print(40 * "-")
account.deposit(70)
print(f"Баланс после пополнения: {account.balance} руб.")
account.withdraw(100)
print(f"Баланс после снятия: {account.balance} руб.")



