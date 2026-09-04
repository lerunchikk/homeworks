"""Разработайте класс Student, который хранит информацию о
студенте: имя, список курсов и оценки. Реализуйте методы
для расчета среднего балла и добавления новых курсов.
Создайте группу студентов и найдите студента с лучшей
успеваемостью
Добавьте метод для вывода информации о незавершенных
курсах
Реализуйте функцию, которая формирует список отличников """

class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []
        self._grades = {}
    def add_courses(self,course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
        else:
            print(f"Этот курс {course_name} уже есть в списке ")
    def add_grade(self,course_name,grade):
        if course_name not in self.courses:
            raise ValueError (f"Студент не записан на этот курс {course_name}")
        if not (1<= grade <=10):
            raise ValueError("Оценка должна быть от 1 до 10")
        self._grades[course_name] = grade

    @property
    def average_grade(self):
        if not self._grades:
            return 0
        return sum(self._grades.values())/len(self._grades)
    def incomplete_courses(self):
        incomplete = [course for course in self.courses if course not in self._grades]
        return incomplete
    def get_info(self):
      print (f"Студент:{self.name} , Средний балл:{self.average_grade}")
def find_best_student(student_list):
    if not student_list:
        return None
    best_student = max(student_list,key = lambda x:x.average_grade )
    return best_student
def list_best_student(student_list):
    return [ student for student in student_list if student.average_grade >8]

student1 = Student("Маша")
student2 = Student("Петя")
student3 = Student("Вася")

student1.add_courses("Математика")
student1.add_courses("Физика")
student1.add_courses("Информатика")

student2.add_courses("Математика")
student2.add_courses("Физика")

student3.add_courses("Информатика")
student3.add_courses("Физика")

student1.add_grade("Математика",8)
student1.add_grade("Физика",8)

student2.add_grade("Математика", 10)
student2.add_grade("Физика", 9)

student3.add_grade("Физика", 9)


print("Незавершенные курсы")
print(f" У студента {student1.name} :{student1.incomplete_courses()}")
print(f" У студента {student2.name} :{student2.incomplete_courses()}")
print(f" У студента {student3.name} :{student3.incomplete_courses()}")

group = [student1,student2,student3]
best = find_best_student(group)
print("Лучший студент группы")
best.get_info()
print()

best_student = list_best_student(group)
print("Список отличников с баллом больше 8")
for x in best_student:
    x.get_info()


