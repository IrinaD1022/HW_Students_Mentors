class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if not self.grades:
            return 0
        else:
            sum_grades = 0
            len_grades = 0
            for grades in self.grades.values():
                sum_grades += sum(grades)
                len_grades += len(grades)   
            return round(sum_grades / len_grades, 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} \
        \nСредняя оценка за домашние задания: {self.average_grade()} \
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __eq__(self, student):
        if not isinstance(student, Student):
            raise Exception('Неверный тип данных')
        else:
            return self.average_grade() == student.average_grade()

    def __lt__(self, student):
        if not isinstance(student, Student):
            raise Exception('Неверный тип данных')
        else:
            return self.average_grade() < student.average_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        else:
            sum_grades = 0
            len_grades = 0
            for grades in self.grades.values():
                sum_grades += sum(grades)
                len_grades += len(grades)   
            return round(sum_grades / len_grades, 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname} \
          \nСредняя оценка за лекции: {self.average_grade()}'

    def __eq__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            raise Exception('Неверный тип данных')
        else:
            return self.average_grade() == lecturer.average_grade()

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            raise Exception('Неверный тип данных')
        else:
            return self.average_grade() < lecturer.average_grade()


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def average_grade_course(persons, course):
    sum_grades = 0
    len_grades = 0
    for person in persons:
        if (not isinstance(person, Lecturer) and 
            not isinstance(person, Student)):
            continue          
        if course in person.grades:
            sum_grades += sum(person.grades[course])
            len_grades += len(person.grades[course])
    return 0 if len_grades == 0 else round(sum_grades / len_grades, 2)

student1 = Student('Иван', 'Петров', 'М')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Анна','Сидорова','Ж')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.finished_courses += ['Введение в программирование']

lect1 = Lecturer('Олег', 'Булыгин')
lect1.courses_attached += ['Python']

lect2 = Lecturer('Елена','Никитина')
lect2.courses_attached += ['Python']
lect2.courses_attached += ['Java']

rev1 = Reviewer('Алена','Батицкая')
rev1.courses_attached += ['Git']

rev2 = Reviewer('Петр','Кукушкин')
rev2.courses_attached += ['Python']
rev2.courses_attached += ['Java']

rev1.rate_hw(student1, 'Git', 9)
rev1.rate_hw(student1, 'Git', 10)
rev1.rate_hw(student1, 'Git', 7)

rev2.rate_hw(student1, 'Python', 7)
rev2.rate_hw(student1, 'Python', 8)
rev2.rate_hw(student1, 'Python', 5)

rev2.rate_hw(student2, 'Python', 10)
rev2.rate_hw(student2, 'Python', 8)
rev2.rate_hw(student2, 'Python', 6)

rev2.rate_hw(student2, 'Java', 9)
rev2.rate_hw(student2, 'Java', 10)

student1.rate_lecturer(lect1, 'Python', 10)
student1.rate_lecturer(lect2, 'Python', 9)
student2.rate_lecturer(lect1, 'Python', 9)
student2.rate_lecturer(lect2, 'Python', 8)
student2.rate_lecturer(lect2, 'Java', 10)

print('Студенты:')
print(student1)
print()
print(student2)
print()

if student1 == student2:
    print('У студентов одинаковые средние оценки за домашние задания')
elif student1 < student2:
    print(f'По среднему баллу {student2.name} {student2.surname} лучше')
else:
    print(f'По среднему баллу {student1.name} {student1.surname} лучше')

print('Лекторы:')
print(lect1)
print()
print(lect2)
print()

if lect1 == lect2:
    print('У студентов одинаковые средние оценки за домашние задания')
elif lect1 < lect2:
    print(f'По среднему баллу {lect2.name} {lect2.surname} лучше')
else:
    print(f'По среднему баллу {lect1.name} {lect1.surname} лучше')

print('Проверяющие:')
print(rev1)
print()
print(rev2)
print()

print(f'Средняя оценка за ДЗ по курсу Python: \
{average_grade_course([student1, student2],"Python")}')
print(f'Средняя оценка за лекции по курсу Python: \
{average_grade_course([lect1, lect2],"Python")}')