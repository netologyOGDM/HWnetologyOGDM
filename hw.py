class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecturers_grades = {}  # Словарь для хранения оценок лекторов
    
    def add_lecturer_grade(self, lecturer, course, grade):
        """Метод для добавления оценки лектору"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            
            if course in self.lecturers_grades:
                self.lecturers_grades[course] += [grade]
            else:
                self.lecturers_grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок
        

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
        
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_lecturer = Lecturer('name1', 'surname1')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('name2', 'surname2')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'Python', 10)

best_student.add_lecturer_grade(cool_lecturer, 'Python', 9)
best_student.add_lecturer_grade(cool_lecturer, 'Python', 9)
best_student.add_lecturer_grade(cool_lecturer, 'Python', 9)
 
print(best_student.grades)
print(cool_lecturer.grades)