import curses
from domains.Student import Student #unecessary
from domains.Course import Course #unecessary

class OutputManager:
    def __init__(self, stdscr, students, courses):
        self.stdscr = stdscr
        self.students = students
        self.courses = courses

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