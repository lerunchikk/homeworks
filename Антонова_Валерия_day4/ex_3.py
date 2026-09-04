shop_list = ["хлеб","молоко"]
print(f"Исходный список shop_list: {shop_list}\nid(shop_list):{id(shop_list)}")
fake_copy = shop_list
print(f"Список fake_copy:{fake_copy}\nid(fake_copy):{id(fake_copy)}")
true_copy = shop_list.copy()
print(f"Список true_copy:{true_copy}\nid(true_copy):{id(true_copy)}")
fake_copy.append("сыр")
true_copy.remove("хлеб")
print(f"Тождественность shop_list is fake_copy: {shop_list is fake_copy}\nТождественность shop_list is true_copy:{shop_list is true_copy}\nCписок shop_list после изменений:{shop_list}\nСписок fake_copy после изменений:{fake_copy}\nСписок true_copy после изменений{true_copy}")