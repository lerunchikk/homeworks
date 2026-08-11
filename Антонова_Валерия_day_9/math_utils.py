def square(number):
    return number ** 2
def cube(number):
    return number ** 3
def is_even(number):
    return number % 2 == 0
def factorial(number):
     if number <=1:
         return 1
     return number * factorial(number - 1)
def max_of_two(a,b):
    if a>b:
        return a
    return b

