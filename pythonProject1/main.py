class Student:


    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 1)
        return res


    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Разные категории людей не сравниваем.")
        return self.avg_rate() < other.avg_rate()


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}'



class Mentor:
    def __init__(self, name, surname, courses_attached):

        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}


    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 1)
        return res


    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Разные категории людей не сравниваем.")
        return self.avg_rate() < other.avg_rate()


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}'

class Reviewer(Mentor):
    def __init__(selfself, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Иван', 'Иванов', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['C+']


lecturer_1=Lecturer('Some', 'Buddy', 'Python')
lecturer_2=Lecturer('Василий', 'Васильков', 'C+')

reviewer_1 = Reviewer('Some', 'Бадди', 'Python')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Петр', 'Петров', 'C+')
reviewer_2.courses_attached += ['C+']



reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)



student_1.rate_lect(lecturer_1, 'Python', 10)
student_2.rate_lect(lecturer_1, 'C+', 10)
student_1.rate_lect(lecturer_1, 'C+', 10)
student_2.rate_lect(lecturer_1, 'Python', 10)
student_1.rate_lect(lecturer_1, 'C+', 10)
student_2.rate_lect(lecturer_1, 'C+', 10)
student_1.rate_lect(lecturer_1, 'Python', 9)

student_1.rate_lect(lecturer_2, 'Python', 10)
student_2.rate_lect(lecturer_2, 'C+', 10)
student_1.rate_lect(lecturer_2, 'C+', 8)
student_2.rate_lect(lecturer_2, 'Python', 10)
student_1.rate_lect(lecturer_2, 'C+', 9)
student_2.rate_lect(lecturer_2, 'C+', 10)
student_1.rate_lect(lecturer_2, 'Python', 9)



print(reviewer_1)
print()
print(lecturer_1)
print()
print(student_1)
print()
print('Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:')
print('lecturer_1 < lecturer_2 ',lecturer_1 < lecturer_2)
print('lecturer_1 > lecturer_2 ',lecturer_1 > lecturer_2)
print()
print('student_1 < student_2 ',student_1 < student_2)
print('student_1 > student_2 ',student_1 > student_2)



