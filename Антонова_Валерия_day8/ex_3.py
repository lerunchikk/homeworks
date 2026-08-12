def is_palidrome(text):
    text = text.replace(" ","").lower()
    print(f"Первоначальная строка или слово: {text}")
    print(f"Обратная строка или слово: {text[::-1]}")
    if text == text[::-1]:
        return True
    else:
         return False
print(is_palidrome("Мадам"))
print(is_palidrome("Сегодня бЫла чудЕсная ПОгода"))

