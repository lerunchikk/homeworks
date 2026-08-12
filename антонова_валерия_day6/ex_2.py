packets = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1]
count = 0
zero_count = 0
for i in packets:
    if i == 1:
      count +=1
      zero_count = 0
    else:
          zero_count +=1
          if zero_count == 2:
           print("Обнаружен критический сбой сети! Соединение разорвано")
           break
print(f"Количество успешно обработанных пакетов:{count}")





















