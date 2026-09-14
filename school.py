class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        print(f"Hello, my name is {self.name} and my email is {self.email}.")


class Student(Person):
    total_students = 0
    students = []

    def __init__(self, name, email, grade):
        super().__init__(name, email)
        self.__grade = grade
        self.courses = []

        Student.total_students += 1
        Student.students.append(self)

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self.__grade = value
        else:
            print("Grade must be between 0 and 100")

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def introduce(self):
        super().introduce()
        print(f"Hi, I am {self.name} and I am a student with a grade of {self.__grade}.")


class Teacher(Person):
    total_teachers = 0
    teachers = []

    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
        self.courses = []

        Teacher.total_teachers += 1
        Teacher.teachers.append(self)

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def introduce(self):
        super().introduce()
        print(f"I am a {self.subject} teacher.")


class Course:
    total_courses = 0
    courses = []

    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []

        Course.total_courses += 1
        Course.courses.append(self)

        teacher.add_course(self)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_course(self)
            print(f"{student.name} has been enrolled in the course {self.course_name}.")
        else:
            print(f"{student.name} is already enrolled in the course {self.course_name}.")

    def show_students(self):
        print(f"Students enrolled in {self.course_name}:")

        if len(self.students) == 0:
            print("No students enrolled yet.")
            return

        for student in self.students:
            print(f"- {student.name} (Grade: {student.grade})")


def find_student(name):
    for student in Student.students:
        if student.name == name:
            return student
    return None


def find_teacher(name):
    for teacher in Teacher.teachers:
        if teacher.name == name:
            return teacher
    return None


def find_course(name):
    for course in Course.courses:
        if course.course_name == name:
            return course
    return None


def menu():
    print("\nWelcome to the School Management System")
    print("Total Students:", Student.total_students)
    print("Total Teachers:", Teacher.total_teachers)
    print("Total Courses:", Course.total_courses)
    print("=========================================================")
    print("1. Create Student")
    print("2. Create Teacher")
    print("3. Create Course")
    print("4. Add Student to Course")
    print("5. Show Students in Course")
    print("6. Exit")


def main():
    while True:
        menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            grade = int(input("Enter student grade: "))

            if find_student(name):
                print("A student with this name already exists.")
            else:
                student = Student(name, email, grade)
                print(f"Student {name} created successfully.")

        elif choice == "2":
            name = input("Enter teacher name: ")
            email = input("Enter teacher email: ")
            subject = input("Enter teacher subject: ")

            if find_teacher(name):
                print("A teacher with this name already exists.")
            else:
                teacher = Teacher(name, email, subject)
                print(f"Teacher {name} created successfully.")

        elif choice == "3":
            course_name = input("Enter course name: ")

            if find_course(course_name):
                print("A course with this name already exists.")
                continue

            teacher_name = input("Enter teacher name for the course: ")
            teacher = find_teacher(teacher_name)

            if teacher is None:
                print("No teacher found. Please create the teacher first.")
                continue

            course = Course(course_name, teacher)
            print(f"Course {course_name} created successfully.")

        elif choice == "4":
            course_name = input("Enter course name: ")
            course = find_course(course_name)

            if course is None:
                print("No course found. Please create the course first.")
                continue

            student_name = input("Enter student name: ")
            student = find_student(student_name)

            if student is None:
                print("No student found. Please create the student first.")
                continue

            course.add_student(student)

        elif choice == "5":
            course_name = input("Enter course name: ")
            course = find_course(course_name)

            if course is None:
                print("No course found.")
                continue

            course.show_students()

        elif choice == "6":
            print("Thank you for using the School Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()