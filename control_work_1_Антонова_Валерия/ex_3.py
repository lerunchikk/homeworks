grades = [78, 91, 56, 83, 95, 61, 88]
new_grades = list(map(lambda x:x+5,filter(lambda num:num>=60, grades)))
print(new_grades)