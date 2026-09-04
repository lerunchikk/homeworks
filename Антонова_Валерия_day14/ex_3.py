"""Дана директория:
project/
data.txt
config.json
image.png
users.txt
README.md
Напишите программу, которая с помощью os.listdir():
● получает список содержимого директории;
● находит только файлы с расширением .txt;
● выводит их имена;
● считает их количество
"""
import os
files = os.listdir("project")
txt_files = []
for i in files:
    if i.endswith("txt"):
        txt_files.append(i)
print(f"Файлы с расширением txt:")
for file in txt_files:
    print(file)
print(f"Количество файлов с расширением txt: {len(txt_files)}")

