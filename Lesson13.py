# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

class Student(Person):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying")

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class Academy:
    def __init__(self, name, students=None, teachers=None, subjects=None):
        self.name = name
        self.students = students
        self.teachers = teachers
        self.subjects = subjects

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_subject(self, subject):
        self.subjects.append(subject)

teacher1 = Teacher("Сухомлинський Василь", 40, "Male", "Math")
teacher2 = Teacher("Алчевська Христина", 25, "Female", "Physics")

student1 = Student("Сергій", 20, "Male", "A")
student2 = Student("Анна", 19, "Female", "B")

math_subject = Subject("Mathematics", teacher1)
physics_subject = Subject("Physics", teacher2)

academy = Academy("My Academy", [student1, student2], [teacher1, teacher2], [math_subject, physics_subject])

for student in academy.students:
    student.study()

for teacher in academy.teachers:
    teacher.teach()