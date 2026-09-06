"""Разработайте систему отправки уведомлений
пользователям.
1. Создайте общий базовый интерфейс для уведомлений.
Отправка сообщения должна выполняться через
единый метод.
2. Реализуйте отдельные классы для:
○ Email;
○ SMS;
○ Push.
3. Каждый способ отправки должен иметь собственное
поведение.
4. Создайте функцию, которая получает список
уведомлений и отправляет через них одно сообщение.
Функция должна работать с разными типами
уведомлений через полиморфизм, без проверки
конкретного класса объекта.
5. Добавьте возможность создавать уведомление
альтернативным способом из конфигурации, например
из словаря с настройками получателя.
6. Добавьте статический метод для проверки
корректности данных получателя.
7. Создайте собственную иерархию исключений для
ошибок системы уведомлений. Предусмотрите как
минимум:
○ некорректного получателя;
○ ошибку отправки уведомления.
8. Реализуйте __str__(), чтобы объекты уведомлений
имели понятное строковое представление.
"""
from abc import ABC,abstractmethod
class NotificationError(Exception):
    pass

class InvalidRecipientError(NotificationError):
    def __init__(self,recipient,reason):
        self.recipient = recipient
        self.reason = reason
        super().__init__(f"Некорректный получать {self.recipient}:{self.reason} ")

class SendNotificationError(NotificationError):
    def __init__(self,notification_type,recipient,reason):
        self.notification_type = notification_type
        super().__init(....)

        super().__init__(f"Ошибка отправки уведомления {self.notification_type} на {self.recipient}:{self.reason}")

class Notification(ABC):
    def __init__(self,recipient,message):
                super().__init(....)

    @abstractmethod
    def send(self):
        pass

    @classmethod
    def from_config(cls,config):
        return cls(config["recipient"], config["message"])

    @staticmethod
    def is_valid_recipient(recipient):
        return isinstance(recipient,str) and len(recipient.strip()) > 0

class EmailNotification(Notification):
    def send(self,):
        if "@" not in self.recipient:
            raise  InvalidRecipientError("Некорекктный email")
        print(f"[Email] Отправка на {self.recipient}:{self.message}")
    def __str__(self):
        return f"Email({self.recipient}):{self.message}"

class SMSNotification(Notification):
    def send(self):
        if not self.recipient.startswith("+"):
            raise InvalidRecipientError("Номер должен начинатся с +")
        print(f"[Email] Отправка на {self.recipient}:{self.message}")
    def __str__(self):
        return  f"SMS({self.recipient}):{self.message}"

class PushNotification(Notification):
    def send(self):
        if not self.recipient:
            raise InvalidRecipientError("Пустое уведомление")
        print(f"[Push] Отправка на {self.recipient}: {self.message}")

    def __str__(self):
        return f"Push({self.recipient}): {self.message}"

def send_notifications(notifications):
    for notification in notifications:
        try:
            notification.send()
        except NotificationError as e:
            print(f"ОшибкаЖ{e}")

email = EmailNotification("user@example.com", "Привет")
sms = SMSNotification("+3751234567", "Ваш код: 1234")
push = PushNotification("user-123", "Новое сообщение")

print(email)
print(sms)
print(push)

notifications = [email, sms, push]
send_notifications(notifications)

config = {'recipient': 'admin@mail.com', 'message': 'Системное сообщение'}
email_from_config = EmailNotification.from_config(config)
email_from_config.send()










