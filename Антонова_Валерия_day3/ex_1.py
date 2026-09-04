name = input("Введите свое имя:")
weight = float(input("Введите свой вес:"))
growth = float(input("Введите свой рост:"))
imt = weight/(growth ** 2)
imt_1 = int(imt)
print(f"--- Ваши данные ---\nИмя:{name}\nВес:{weight}\nРост:{growth}\nИМТ = {imt_1}")

