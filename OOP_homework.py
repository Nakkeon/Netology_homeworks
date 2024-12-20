class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in self.courses_in_progress
            and course in lector.courses_attached and
                grade >= 0 and grade <= 10):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        if len(self.grades) == 0:
            return 0
        points = 0
        for course in self.grades:
            points += self.average_per_course(course)
        return points / len(self.grades)

    def average_per_course(self, course):
        if course not in self.grades:
            return 0
        points = 0
        for grade in self.grades[course]:
            points += grade
        return points / len(self.grades[course])

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average()}\n"
            f"Курсы в процессе изучения: "
            f"{', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: "
            f"{', '.join(self.finished_courses)}"
        )
        
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average() < other.average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return other < self

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return not (self < other) and not (other < self)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        if len(self.grades) == 0:
            return 0
        points = 0
        for course in self.grades:
            points += self.average_per_course(course)
        return points / len(self.grades)

    def average_per_course(self, course):
        if course not in self.grades:
            return 0
        pointers = 0
        for grade in self.grades[course]:
            pointers += grade
        return pointers / len(self.grades[course])

    def __str__(self):
        return (
            f'Имя: {self.name} \n'
            f'Фамилия: {self.surname} \n'
            f'Средняя оценка за лекции: {self.average()}'
        )
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average() < other.average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return other < self

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return not (self < other) and not (other < self)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

# Полевые испытания

student1 = Student('Елена', 'Антонова', 'жен')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Даниил', 'Орлов', 'муж')
student2.courses_in_progress += ['C#']
student2.finished_courses += ['Git']

reviewer1 = Reviewer('Сергей', 'Бобров')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Ольга', 'Бобкова')
reviewer2.courses_attached += ['C#']

lecturer1 = Lecturer('Марат', 'Храмов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Семён', 'Соколов')
lecturer2.courses_attached += ['C#']


print('--ПРОВЕРЯЮЩИЕ')
print(reviewer1)
print()
print(reviewer2)
print()

print('--СТУДЕНТЫ')
reviewer1.rate_student(student1, 'Python', 10)
reviewer2.rate_student(student2, 'C#', 9)
print(student1)
print()
print(student2)
print()
if student1 > student2:
    print('Оценка студента 1 выше')
elif student2 > student1:
    print('Оценка студента 2 выше')
else:
    print('Оценки студентов одинаковы')
print()

print('--ЛЕКТОРЫ')
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'C#', 8)
print(lecturer1)
print()
print(lecturer2)
print()
if lecturer1 > lecturer2:
    print('Оценка лектора 1 выше')
elif lecturer2 > lecturer1:
    print('Оценка лектора 2 выше')
else:
    print('Оценки лекторов одинаковы')
print()

def average_student_rating_on_course(students, course):
    pointers = 0
    students_count = 0
    for student in students:
        if course in student.grades:
            pointers += student.average_per_course(course)
            students_count += 1
    if students_count == 0:
        return 0
    return pointers / students_count


def average_lecturer_rating_on_course(lecturers, course):
    pointers = 0
    lecturers_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            pointers += lecturer.average_per_course(course)
            lecturers_count += 1
    if lecturers_count == 0:
        return 0
    return pointers / lecturers_count


print('Средняя оценка по курсу Python: ', sep='')
print(average_student_rating_on_course([student1, student2], 'Python'))
print('Средняя оценка по курсу C#: ', sep='')
print(average_lecturer_rating_on_course([lecturer1, lecturer2], 'C#'))