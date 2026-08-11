import math_utils
print("Задание 1")
number = 5
print(f"Число: {number}, Квадрат из числа = {math_utils.square(number)}")

print("Задание 2")
print(f"Число: {number}, Куб числа = {math_utils.cube(number)}")

print("Задание 3")
for num in [2,3,4,5]:
    result = math_utils.is_even(num)
    print(f"Тестируемое число: {num}, Четные числа:{result}")

print("Задание 4")
number = 5
print(f"Число:{number}, Факториал число = {math_utils.factorial(number)}")

print("Задание 5")
print(f"Максимум из 2 чисел: {math_utils.max_of_two(4,8)}")
