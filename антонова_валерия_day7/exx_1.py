
logs = [ 200, 200, 404, 200, 500, 200, 503, 200, 200, 404, 500, 200, 503 ]
count_requests = 0
count_klient_error = 0
count_server_error = 0
consecutive_server_errors = 0
for i in logs:
    if i == 200:
     count_requests +=1
     consecutive_server_errors = 0
    elif i == 404:
     count_klient_error +=1
     consecutive_server_errors = 0
    elif i == 500 or i == 503:
     count_server_error +=1
     consecutive_server_errors +=1
     if consecutive_server_errors == 2:
      print("Сервер считается недоступным")
      break
print(f"Количество успешных запросов:{count_requests}\nКоличество клиентских ошибок:{count_klient_error}\nКоличество серверных ошибок:{count_server_error}\nКоличество серверных ошибок встречающихся подряд:{consecutive_server_errors} ")
# Ответ на вопрос: Сложность алгоритма - O(n),т.к. break позволяет не делать лишних проверок после нахождения ошибки, но не меняет Big O в худшем случае, всё равно нужно проверить все элементы.