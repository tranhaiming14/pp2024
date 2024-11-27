import math
import numpy as np
# Changed mark dictionary from Course to Student for a more intuitive understanding
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}  
        self.gpa = 0.0
class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
class StudentManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            self.input_student_info()

    def input_student_info(self):
        student_id = input("Enter the student ID here: ")
        name = input("Enter student's name: ")
        student = Student(student_id, name)
        self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            self.input_course_info()

    def input_course_info(self):
        course_id = input("Enter the course ID here: ")
        name = input("Enter course name: ")
        while any(course_id == course.course_id for course in self.courses):
            print("Course id not valid!")
            course_id = input("Enter the course ID here: ")
        credits = input("Enter the number of credits: ")
        course = Course(course_id, name, credits)
        self.courses.append(course)

    def input_marks(self):
        for student in self.students:
            print(f"Enter the mark for student {student.name}:")
            for course in self.courses:
                mark = float(input(f"Enter the mark for course {course.name}: "))
                mark = math.floor(mark * 10) / 10.0
                student.marks[course.course_id] = mark
    def calculate_gpa(self):
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for course in self.courses:
                if course.course_id in student.marks:
                    mark = student.marks[course.course_id]
                    total_weighted_marks += mark * course.credits
                    total_credits += course.credits
            student.gpa = total_weighted_marks / total_credits if total_credits > 0 else 0
    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)

    def display_students_by_gpa(self):
        self.sort_students_by_gpa()
        for student in self.students:
            gpa = self.gpa
            print(f"Student {student.name} has a GPA of {gpa:.2f}")

    def display_marks(self):
        while True:
            student_id = input("Enter the student ID to view marks: ")
            if student_id == "out":
                break
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                for course in self.courses:
                    mark = student.marks.get(course.course_id, "No marks")
                    print(f"Student {student.name} has {mark} mark in course {course.course_id}")
            else:
                print("Student not found.")

def main():
    manager = StudentManager()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()
    manager.calculate_gpa()
    manager.display_marks()
    manager.display_students_by_gpa()
if __name__ == "__main__":
    main()