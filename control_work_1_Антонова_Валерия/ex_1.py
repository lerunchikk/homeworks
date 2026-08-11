numbers = list(map(int, input("Введите последовательность целых чисел через пробел:").split()))
maxxi = numbers[0]
minni = numbers[0]
summ = 0
for num in numbers:
    if num > maxxi:
        maxxi = num
    if num < minni:
        minni = num
    if num > 0:
        summ +=num
unique_numbers = sorted(set(numbers))
print(f"Максимальное число:{maxxi}\nМинимальное число:{minni}\nСумма положительных чисел:{summ}\nУникальные числа:{unique_numbers}")
