from random import randint
random_number = randint(1,50)
attempt = 5
for i in range(1,attempt+1):
    number = int(input("Введите число:"))
    if number == random_number:
        print("Поздравляю, вы отгадали число")
        break
    elif number> random_number:
        print("Меньше!")
    else:
        print("Больше!")
else:
    print(f"Попытки закончились, правильное число было: {random_number}")

