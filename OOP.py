class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"{self.name} {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecture(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.gradescourse.append(grade)
            else:
                self.gradescourse = grade
        else:
            print("Ошибка: Студент не привязан к курсу или курс не закреплен за лектором.")

    def get_average_grade(self):

        total_grades = sum(grades.values())
        for course, grades in self.grades.items():
            return total_grades / len(self.grades) if len(self.grades) else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{self.name} {self.surname}: {average_grade}"
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка: Студент не привязан к курсу или курс не закреплен за проверяющим.")

    def get_average_grade(self):
        total_grades = sum(grades.values())
        for course, grades in self.grades.items():
            return total_grades / len(self.grades) if len(self.grades) else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{self.name} {self.surname}: {average_grade}"
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.gradescourse.append(grade)
            else:
                lecturer.gradescourse = grade
        else:
                print("Ошибка: Лектор не привязан к курсу или студент не изучает этот курс.")

    def get_average_grade(self):
        total_grades = sum(grades.values())
        for course, grades in self.grades.items():
            return total_grades / len(self.grades) if len(self.grades) else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{self.name} {self.surname}: {average_grade}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.gradescourse.append(grade)
            else:
                student.gradescourse = grade
        else:
            print("Ошибка: Студент не привязан к курсу или курс не закреплен за проверяющим.")

    def get_average_grade(self):
        total_grades = sum(grades.values())
        for course, grades in self.grades.items():
            return total_grades / len(self.grades) if len(self.grades) else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{self.name} {self.surname}: {average_grade}"



student1 = Student("Ruoy", "Eman")
student1.courses_in_progress.append("Python")
student2 = Student("Jane", "Doe")
student2.courses_in_progress.append("Python")

lecturer1 = Lecturer("John", "Smith")
lecturer1.courses_attached.append("Python")
lecturer2 = Lecturer("Emily", "Clark")
lecturer2.courses_attached.append("Python")

reviewer = Reviewer("Some", "Buddy")
reviewer.courses_attached.append("Python")


reviewer.rate_hw(student1, "Python", 8)
reviewer.rate_hw(student1, "Python", 10)
reviewer.rate_hw(student2, "Python", 7)

student1.rate_lecture(lecturer1, "Python", 9)
student1.rate_lecture(lecturer2, "Python", 8)


print(student1)
print(lecturer1)
print(reviewer)


print("Средняя оценка за домашние задания по курсу Python:", average_student_grade([student1, student2], "Python"))
print("Средняя оценка за лекции по курсу Python:", average_lecture_grade([lecturer1, lecturer2], "Python"))  


