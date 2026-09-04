balans = input("Введите баланс счета:")
summa = input("Введите сумму переревода:")
try:
    balans_num = int(balans)
    summa_num = int(summa)
    if summa_num>balans_num:
        raise ValueError("Недостаточный баланс.Баланс счета не может быть меньше суммы перевода")
except ValueError as error:
    print(f"Ошибка:{error}")
else:
    print(f"Новый баланс:{balans_num-summa_num}")
    print("Операция выполнена успешно")
finally:
    print("Операция завершена")