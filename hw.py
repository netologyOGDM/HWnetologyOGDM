class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.add_lecturers_grades = {}  # Словарь для хранения оценок лекторов

    def _calculate_average_grade(self):
        total_sum = 0
        grades_count = 0
        for course, grades in self.grades.items():
            total_sum += sum(grades)
            grades_count += len(grades)

        if grades_count == 0:
            return 0
        return round(total_sum / grades_count, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'<' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() < other._calculate_average_grade()
        print(f'\n{self.name} имеет средний балл меньше, чем {other.name}: {result}')
        return result

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'<=' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() <= other._calculate_average_grade()
        print(f'{self.name} имеет средний балл меньше или равен, чем {other.name}: {result}')
        return result

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() > other._calculate_average_grade()
        print(f'{self.name} имеет средний балл больше, чем {other.name}: {result}')
        return result

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>=' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() >= other._calculate_average_grade()
        print(f'{self.name} имеет средний балл больше или равен, чем {other.name}: {result}')
        return result

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'==' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() == other._calculate_average_grade()
        print(f'{self.name} имеет такой же средний балл, как {other.name}: {result}')
        return result

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'!=' not supported between instances of 'Student' and '{type(other).__name__}'")

        result = self._calculate_average_grade() != other._calculate_average_grade()
        print(f'{self.name} имеет другой средний балл, чем {other.name}: {result}')
        return result

    def __str__(self):
        average_grade = self._calculate_average_grade()
        return f'\nprint (some_student)\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {self.courses_in_progress}'

    def add_lecturer_grade(self, lecturer, course, grade):
        """Метод для добавления оценки лектору"""
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.add_lecturer_grade:
                lecturer.add_lecturer_grade[course] += [grade]
            else:
                lecturer.add_lecturer_grade[course] = [grade]

            if course in self.add_lecturers_grades:
                self.add_lecturers_grades[course] += [grade]
            else:
                self.add_lecturers_grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'print(some_mentors)\nИмя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.add_lecturer_grade = {}
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def _calculate_average_grade(self):
        total_sum = 0
        grades_count = 0
        for course, grades in self.add_lecturer_grade.items():  # Используем self.lecturers_grades вместо self.grades1
            total_sum += sum(grades)
            grades_count += len(grades)

        if grades_count == 0:
            return 0
        return round(total_sum / grades_count, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'<' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() < other._calculate_average_grade()
        print(f'\n{self.name} имеет средний балл меньше, чем {other.name}: {result}')
        return result

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'<=' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() <= other._calculate_average_grade()
        print(f'{self.name} имеет средний балл меньше или равен, чем {other.name}: {result}')
        return result

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'>' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() > other._calculate_average_grade()
        print(f'{self.name} имеет средний балл больше, чем {other.name}: {result}')
        return result

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'>=' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() >= other._calculate_average_grade()
        print(f'{self.name} имеет средний балл больше или равен, чем {other.name}: {result}')
        return result

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'==' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() == other._calculate_average_grade()
        print(f'{self.name} имеет такой же средний балл, как {other.name}: {result}')
        return result

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError(f"'!=' not supported between instances of 'Lecturer' and '{type(other).__name__}'")

        result = self._calculate_average_grade() != other._calculate_average_grade()
        print(f'{self.name} имеет другой средний балл, чем {other.name}: {result}')
        return result

    def __str__(self):
        average_grade = self._calculate_average_grade()
        return f'print(some_lecturer)\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_student(self, student, course, grade):

        """Метод для добавления оценки студенту"""
        if isinstance(student, Student) and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'\nprint(some_reviewer)\nИмя: {self.name}\nФамилия: {self.surname}'


best_student1 = Student('Ruoy', 'Eman', 'M')
best_student1.courses_in_progress += ['Python','Git']
best_student2 = Student('Sarah', 'Megan', 'F')
best_student2.courses_in_progress += ['Python','Введение в програмирование']

cool_lecturer1 = Lecturer('Nikolay', 'Ivanov')
cool_lecturer1.courses_attached += ['Python','Git']
cool_lecturer2 = Lecturer('Olga', 'Petrova')
cool_lecturer2.courses_attached += ['Python','Введение в програмирование']

cool_reviewer1 = Reviewer('Mihail', 'Volkov')
cool_reviewer1.courses_attached += ['Python','Git']
cool_reviewer2 = Reviewer('Irina', 'Zaiceva')
cool_reviewer2.courses_attached += ['Python','Введение в програмирование']

cool_reviewer1.rate_student(best_student1, 'Python', 10)
cool_reviewer1.rate_student(best_student1, 'Python', 10)

cool_reviewer2.rate_student(best_student2, 'Python', 5)
cool_reviewer2.rate_student(best_student2, 'Python', 5)

# Студент ставит оценку лектору
best_student1.add_lecturer_grade(cool_lecturer1, 'Python', 10)
best_student1.add_lecturer_grade(cool_lecturer1, 'Python', 9)

best_student2.add_lecturer_grade(cool_lecturer2, 'Python', 10)
best_student2.add_lecturer_grade(cool_lecturer2, 'Python', 10)


print(best_student1 < best_student2)
print(best_student1 <= best_student2)
print(best_student1 > best_student2)
print(best_student1 >= best_student2)
print(best_student1 == best_student2)
print(best_student1 != best_student2)

print(cool_lecturer1 < cool_lecturer2)
print(cool_lecturer1 <= cool_lecturer2)
print(cool_lecturer1 > cool_lecturer2)
print(cool_lecturer1 >= cool_lecturer2)
print(cool_lecturer1 == cool_lecturer2)
print(cool_lecturer1 != cool_lecturer2)

print (best_student1)
print (best_student2)
print (cool_reviewer1)
print (cool_reviewer2)
print (cool_lecturer1)
print (cool_lecturer2)