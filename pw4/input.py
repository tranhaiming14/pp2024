import curses
from domains.Student import Student
from domains.Course import Course
import math
class InputManager:
    def __init__(self, stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr

    def input_students(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the number of students: ")
        num_students = int(self.stdscr.getstr().decode())
        for _ in range(num_students):
            self.input_student_info()

    def input_student_info(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the student ID here: ")
        student_id = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter student's name: ")
        name = self.stdscr.getstr().decode()
        student = Student(student_id, name)
        self.students.append(student)

    def input_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the number of courses: ")
        num_courses = int(self.stdscr.getstr().decode())
        for _ in range(num_courses):
            self.input_course_info()

    def input_course_info(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the course ID here: ")
        course_id = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter course name: ")
        name = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter the number of credits: ")
        credits = float(self.stdscr.getstr().decode())
        course = Course(course_id, name, credits)
        self.courses.append(course)
    def input_marks(self):
        for student in self.students:
            self.stdscr.clear()
            self.stdscr.addstr(f"Enter the marks for student {student.name}:\n")
            for course in self.courses:
                self.stdscr.addstr(f"Enter the mark for course {course.name}: ")
                mark = float(self.stdscr.getstr().decode())
                mark = math.floor(mark * 10) / 10.0
                student.marks[course.course_id] = mark
