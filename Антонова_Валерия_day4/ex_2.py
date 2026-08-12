cost_1 = int(input("Введите сумму покупки:"))
type = input("Введите тип клиентской зоны (RU,EU или US:")
cost_2 = 0
if type == "RU":
    if cost_1>=5000:
      cost_2 = 0
    else:
       cost_2 = 500
elif type == "EU":
    cost_2 = 1000
elif type == "US":
    if cost_1>=15000:
       cost_2 = 800
    else:
       cost_2 = 2000
sum = cost_1 + cost_2
print(f"total_price = {sum}")