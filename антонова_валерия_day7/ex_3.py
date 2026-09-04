password = "Python2026"
attempt = 5
count = 0
while count < attempt:
    word = input("Введите пароль: ")
    if word == password:
        print("Доступ разрешен ")
        break
    if word == "exit":
        break
    if  count == 4:
        print("Аккаунт заблокирован")
        count +=1
    else:
        print("Попробуйте еще раз ")
        count +=1


