from functools import wraps

def ignore_duplicates(func):
    last_text = None
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal last_text
        if args == last_text:
            print("Повторный вызов проигнорирован")
            return None
        last_text = args
        return func(*args, **kwargs)
    return wrapper
@ignore_duplicates
def send_message(text):
 print(f"Отправлено: {text}")

send_message("Привет")
send_message("Привет")
send_message("Как дела?")
send_message("Как дела?")
send_message("Привет")




