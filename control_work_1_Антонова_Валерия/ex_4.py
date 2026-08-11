def process_numbers(numbers, operation):
    return list(map(operation, numbers))

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def modul(x):
    return abs(x)

numbers = [1, 2, 3, 4]
print("С lambda")
print("Квадрат:", process_numbers(numbers, lambda x: x ** 2))
print("Куб:    ", process_numbers(numbers, lambda x: x ** 3))
print("Модуль: ", process_numbers(numbers, lambda x: abs(x)))

print("\nС обычными функциями")
print("Квадрат:", process_numbers(numbers, square))
print("Куб:    ", process_numbers(numbers, cube))
print("Модуль: ", process_numbers(numbers, modul))