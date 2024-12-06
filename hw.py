class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.сompleted_courses =[]
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
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'<=' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>=' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() >= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'==' not supported between instances of 'Lecturer' and '{type(other).__name__}'")
        return self._calculate_average_grade() == other._calculate_average_grade()


    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'!=' not supported between instances of 'Lecturer' and '{type(other).__name__}'")
        return self._calculate_average_grade() != other._calculate_average_grade()


    def __str__(self):
        average_grade = self._calculate_average_grade()
        return f'print(some_student)\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\nКурсы в процессе изучения: {best_student.courses_in_progress}\nЗавершенные курсы: {best_student.сompleted_courses}'


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
        #self.grades1 = {}  # Словарь для хранения оценок
        #self.add_lecturers_grades = {}  # Словарь для хранения оценок лекторов
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
        if not isinstance(other, Student):
            raise TypeError(f"'<' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() < other._calculate_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'<=' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() <= other._calculate_average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() > other._calculate_average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'>=' not supported between instances of 'Student' and '{type(other).__name__}'")
        return self._calculate_average_grade() >= other._calculate_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'==' not supported between instances of 'Lecturer' and '{type(other).__name__}'")
        return self._calculate_average_grade() == other._calculate_average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            raise TypeError(f"'!=' not supported between instances of 'Lecturer' and '{type(other).__name__}'")
        return self._calculate_average_grade() != other._calculate_average_grade()

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
        return f'print(some_reviewer)\nИмя: {self.name}\nФамилия: {self.surname}'

#course1 = "Python"
#course2 = "Git"
course3 = "Введение в программирование"

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python','Git']
best_student.сompleted_courses += ['Введение в програмирование']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 9.6)

# Студент ставит оценку лектору
best_student.add_lecturer_grade(cool_lecturer, 'Python', 9.9)
best_student.add_lecturer_grade(cool_lecturer, 'Python', 9.9)
best_student.add_lecturer_grade(cool_lecturer, 'Python', 9.9)

print(cool_reviewer)
print(cool_lecturer)
print (best_student)