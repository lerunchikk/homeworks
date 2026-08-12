filename = input("Введите имя файла:")
file_size = float(input("Введите размер файла в мегабайтах:"))
is_admin = True if input("Является ли пользователь администратором(yes/no):") == "yes" else False
if (filename.endswith(".exe") or filename.endswith(".bat")) and is_admin == False:
    print("Доступ запрещен:опасный файл")
elif (filename.endswith(".zip") or filename.endswith(".rar")) and is_admin == True:
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")