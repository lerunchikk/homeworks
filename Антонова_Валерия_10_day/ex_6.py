
students = [
{"name": "Иван", "score": 82},
{"name": "Анна", "score": 95},
{"name": "Петр", "score": 67},
{"name": "Мария", "score": 91},
{"name": "Олег", "score": 73},
{"name": "Елена", "score": 88},
]
sorted_student = list(map(lambda x:f"{x["name"]}:({x["score"]})",
                 sorted(filter(lambda x:x["score"]>=80,students),
                       key = lambda x: x["score"], reverse = True)))
print("\n".join(sorted_student))