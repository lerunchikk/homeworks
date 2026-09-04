def  analyze_grades(*grades):
    if not grades:
        return None
    count = len(grades)
    average = sum(grades) / count
    highest = max(grades)
    lowest = min(grades)
    passed = 0
    for grade in grades:
        if grade>=60:
            passed+=1
    return {
        "count": count,
         "average": average,
         "highest": highest,
         "lowest": lowest,
         "passed": passed
    }
print(analyze_grades(3,5,70,60))