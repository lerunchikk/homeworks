"""
Небольшое задание именно на наследование и
переопределение методов. Создайте базовый класс:
Notification. У него должен быть метод: send(message).
Затем создайте:
● EmailNotification;
● SMSNotification;
● PushNotification.
Каждый класс должен по-своему реализовать send().
Проверить в цикле.
Дополнительное усложнение: добавить в Notification общий
атрибут recipient и использовать super().__init__() в дочерних
классах.
"""


class Notification:
    def __init__(self,recipient):
        self.recipient = recipient
    def send(self,message):
        raise NotImplementedError

class EmailNotification(Notification):
    def __init__(self,recipient):
        super().__init__(recipient)
    def send(self,message):
        print(f"[EMAIL] Отправка письма на {self.recipient}: {message}")

class  SMSNotification(Notification):
    def __init__(self,recipient):
        super().__init__(recipient)
    def send(self,message):
        print(f"[SMS] Отправка cообщения на {self.recipient}: {message}")

class PushNotification(Notification):
    def __init__(self,recipient):
        super().__init__(recipient)
    def send(self,message):
        print(f"[PUSH] Отправка push-уведомления {self.recipient}: {message}")

notification = [EmailNotification("user@recept.com"),SMSNotification("+375(89)345-45-67"),PushNotification("user3456")]
message = "Уведомление отправлено"
print("Все уведомления:")
for x in notification:
    x.send(message)
    print()
