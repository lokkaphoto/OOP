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
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            print("Ошибка: Студент не привязан к курсу или курс не закреплен за лектором.")

    def get_average_grade(self):
        total_grades = sum(grades.values()) for course, grades in self.grades.items()
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
        total_grades = sum(grades.values()) for course, grades in self.grades.items()
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
        total_grades = sum(grades.values()) for course, grades in self.grades.items()
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
        total_grades = sum(grades.values()) for course, grades in self.grades.items()
        return total_grades / len(self.grades) if len(self.grades) else 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{self.name} {self.surname}: {average_grade}"


# Пример использования
student = Student("Иван", "Иванов")
lecturer = Lecturer("Петр", "Петров")
reviewer = Reviewer("Анна", "Иванова")

student.rate_lecture(lecturer, "Математика", 80)
student.rate_lecture(lecturer, "Физика", 90)

lecturer.rate_hw(student, "Математика", 75)
lecturer.rate_hw(student, "Физика", 85)

reviewer.rate_hw(student, "Математика", 85)
reviewer.rate_hw(student, "Физика", 95)

print(student)
print(lecturer)
print(reviewer)