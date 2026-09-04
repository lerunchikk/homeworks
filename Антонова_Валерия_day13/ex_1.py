while True:
    num = input("Введите число от 1 до 100:")
    if num.lower() == "exit":
        print("Программа завершена")
        break
    try:
      number = int(num)
    except ValueError as error:
     print("Ошибка:Необходимо ввести число")
    else:
        if 100 < number or number < 1:
            print("Ошибка: число должно быть от 1 до 100")
        else:
            print(f"Число принято:{number}")
            break






