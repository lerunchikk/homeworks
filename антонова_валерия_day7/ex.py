# Пользователь вводит предложение
# Программа должна:
# 1. Посчитать количество символов
# 2. Посчитать количество слов
# 3. Вывести первое и последнее слово
# 4. Вывести предложение в обратном порядке
# 5. Заменить все буквы "а" на "*"
sentences = input("Введите строку:")
count_symbols = len(sentences)
words = sentences.split()
word_count = len(words)
first_word = words[0]
end_word = words[-1]
new_words = sentences[::-1]
word_new = sentences.replace('а','*').replace('A','*')
(print(f"Количество символов:{count_symbols}\nКоличество слов:{word_count}\nПервое слово:{first_word}\nПоследнее слово:{end_word}\nПредложение в обратном порядке: {new_words}\nЗамена всех а на *:{word_new}"))