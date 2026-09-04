"""Содержимое:
name,price,category
Laptop,1200,Electronics
Phone,800,Electronics
Book,25,Books
Table,300,Furniture
Напишите программу, которая:
● читает CSV;
● выводит названия всех товаров;
● находит товары дороже 500;
● считает их количество;
● выводит самый дорогой товар."""
import csv
with open("product.csv","w",encoding="utf-8") as file:
    file.write("name,price,category\n")
    file.write("Laptop,1200,Electronics\n")
    file.write("Phone,800,Electronics\n")
    file.write("Book,25,Books\n")
    file.write("Table,300,Furniture\n")

products = []
with open("product.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for i in reader:
        i['price'] = int(i["price"])
        products.append(i)

print("Название всех товаров:")
for i in products:
    print(i['name'])

tovars = []
expensive_price = products[0]
print("Товары дороже 500:")
for i in products:
    if i['price']>500:
        tovars.append(i)
        print(i['name'])

    if i['price']>expensive_price['price']:
        expensive_price = i

print(f"Количество товаров дороже 500: {len(tovars)}")
print(f"Самый дорогой товар: {expensive_price['name']}({expensive_price['price']})")
