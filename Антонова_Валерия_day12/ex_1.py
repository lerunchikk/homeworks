from functools import wraps
def repeat(times,separator):
    def parametr(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            results = []
            for i in range(times):
             result = func(*args, **kwargs)
             results.append(str(result))
            return separator.join(results)
        return wrapper
    return parametr
@repeat(times = 3,separator="---")
def greet(name):
    return f"Привет,{name}!"
print(greet("Иван"))

@repeat(times=2, separator="=")
def add(a, b):
 return a + b
print(add(5, 3))




