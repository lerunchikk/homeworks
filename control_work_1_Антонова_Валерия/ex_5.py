products = [
    {"name": "Хлеб", "price": 70, "count": 2},
    {"name": "Молоко", "price": 120, "count": 1},
    {"name": "Сыр", "price": 350, "count": 3},
]
def process_products(products):
    total = 0
    for product in products:
        total += product["price"] * product["count"]

    most_expensive = products[0]["name"]
    max_price = products[0]["price"]
    for product in products:
        if product["price"] > max_price:
            max_price = product["price"]
            most_expensive = product["name"]

    items = 0
    for product in products:
        items += product["count"]

    return {
        "total": total,
        "most_expensive": most_expensive,
        "items": items
    }

result = process_products(products)
print(result)