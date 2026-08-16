from functools import wraps
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
     try:
        return func(*args,**kwargs)
     except ValueError:
        print(f"Ошибка:Некорректное значение")
     except ZeroDivisionError:
        print("Ошибка:Деление на ноль")
     except Exception as e:
         print(f"Ошибка:{e}")
    return wrapper
@handle_errors
def divide(a, b):
 return a / b

@handle_errors
def convert_to_int(value):
    return int(value)

print(divide(4,8))
print(divide(10, 2))
print(divide(10, 0))

print(convert_to_int("100"))
print(convert_to_int("hello"))


