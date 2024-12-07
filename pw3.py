import math
import curses
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
    def __init__(self, stdscr):
        self.students = []
        self.courses = []
        self.stdscr = stdscr

    def input_students(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the number of students: ")
        curses.echo()
        num_students = int(self.stdscr.getstr().decode())
        for _ in range(num_students):
            self.input_student_info()

    def input_student_info(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the student ID here: ")
        curses.echo()
        student_id = self.stdscr.getstr().decode()
        self.stdscr.addstr("Enter student's name: ")
        name = self.stdscr.getstr().decode()
        student = Student(student_id, name)
        self.students.append(student)

    def input_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the number of courses: ")
        curses.echo()
        num_courses = int(self.stdscr.getstr().decode())
        for _ in range(num_courses):
            self.input_course_info()

    def input_course_info(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter the course ID here: ")
        curses.echo()
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
                curses.echo()
                mark = float(self.stdscr.getstr().decode())
                mark = math.floor(mark * 10) / 10.0
                student.marks[course.course_id] = mark

    def calculate_gpa(self, students):
        total_credits = 0
        total_weighted_marks = 0
        for student in students:
            for course in self.courses:
                if course.course_id in student.marks:
                    mark = student.marks[course.course_id]
                    total_weighted_marks += mark * course.credits
                    total_credits += course.credits
            student.gpa = total_weighted_marks / total_credits if total_credits > 0 else 0

    def display_gpas(self):
        self.stdscr.clear()
        self.students.sort(key=lambda student: student.gpa, reverse=True)
        for student in self.students:
            self.stdscr.addstr(f"Student {student.name} has a GPA of {student.gpa}\n")
        self.stdscr.addstr("\nPress any key to continue")
        self.stdscr.refresh()
        self.stdscr.getch()

    def display_marks(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("Enter the student ID to view marks (type 'out' to exit): ")
            curses.echo()
            student_id = self.stdscr.getstr().decode()
            if student_id == "out":
                break
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                for course in self.courses:
                    mark = student.marks.get(course.course_id, "No marks")
                    self.stdscr.addstr(f"Student {student.name} has {mark} mark in course {course.course_id}\n")
            else:
                self.stdscr.addstr("Student not found.\n")
            self.stdscr.addstr("\nPress any key to continue...")
            self.stdscr.refresh()
            self.stdscr.getch()

def main(stdscr):
    curses.cbreak()
    stdscr.clear()
    stdscr.refresh()
    manager = StudentManager(stdscr)

    while True:
        stdscr.clear()
        stdscr.addstr("HaiMinhs Student Management System\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. Display GPAs\n")
        stdscr.addstr("5. Display Marks\n")
        stdscr.addstr("6. Exit\n")
        stdscr.addstr("Choose an option: ")
        curses.echo()
        choice = int(stdscr.getstr().decode())

        if choice == 1:
            manager.input_students()
        elif choice == 2:
            manager.input_courses()
        elif choice == 3:
            manager.input_marks()
        elif choice == 4:
            manager.display_gpas()
        elif choice == 5:
            manager.display_marks()
        elif choice == 6:
            break
        else:
            stdscr.addstr("Invalid option.")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)