"""
Задание 4
Напишите консольную программу, которая работает в цикле:
while True:
command = input("Введите команду: ")
Поддерживаются команды:
● add
● remove
● show
● exit
В программе хранится список:
items = []
Поведение:
● add — запросить число и добавить его в список;
● remove — запросить индекс элемента и удалить его;
● show — вывести все элементы;
● exit — завершить программу.
Необходимо обработать ошибки:
● пользователь ввёл не число при добавлении → ValueError;
● пользователь ввёл некорректный индекс → IndexError;
● пользователь ввёл неизвестную команду → вывести
сообщение об ошибке.
После обработки ошибки программа должна продолжить
работу, а не завершаться.
Дополнительное условие: для команды remove нельзя
проверять индекс через if. Необходимо продемонстрировать
обработку IndexError.
"""
from os import remove

items = []
while True:
    command = input("Введите команду: ")
    if command == "exit":
     print("Программа завершена")
     break
    elif command == "add":
        try:
            number = int(input("Введите число:"))
        except ValueError:
            print("Ошибка: Нужно ввести число")
        else:
            items.append(number)
            print(f"Число успешно добавлено: {number}")
    elif command == "remove":
        try:
            element = int(input("Введите индекс элемента который вы хотите удалить:"))
            removed = items.pop(element)
        except ValueError:
            print("Ошибка:Необходимо ввести число")
        except IndexError:
            print("Ошибка:Неккоретный ввод индекса")
        else:
            print(f"Число под индексом {element} удалено")

    elif command == "show":
        if items:
         print("Все элементы списка")
         for num in items:
            print(num)
        else:
            print("Список элементов пуст")
    else:
        print("Ошибка:Неизвестная команда")






