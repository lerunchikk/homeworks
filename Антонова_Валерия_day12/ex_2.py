from functools import wraps
def limit_calls(limit,message,default):
    def decorator(func):
        count = 0
        @wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal count
            if count >= limit:
                print(message)
                return default
            count+=1
            return func(*args,**kwargs)
        return wrapper
    return decorator

@limit_calls(limit=3,message="Лимит вызовов исчерпан!",default=None)
def get_data(name, age):
 print(f"Получаем данные: {name}, {age}")
 return f"{name}: {age}"
print(get_data("Иван", 20))
print(get_data("Анна", 25))
print(get_data("Петр", 30))
print(get_data("Мария", 22))
print("---------------------")

@limit_calls(2, "Лимит!", 0)
def add(a, b):
 return a + b
print(add(3,5))
print(add(4,6))
print(add(2,1))
print(add(6,7))
print("---------------------")

@limit_calls(3, "Больше нельзя!", [])
def get_items(category):
  return ["item1", "item2"]
print(get_items("text"))
print(get_items("numbers"))
print(get_items("values"))
print(get_items("keys"))


