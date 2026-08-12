def power_factory(power:int):
    def counter(x:int)->int:
        return x ** power
    return counter
square = power_factory(2)
cube = power_factory(3)
print(square(5))
print(cube(3))
print(cube(5))

