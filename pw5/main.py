import curses
from input import InputManager
import os
import json
from zipfile import ZipFile
from output import OutputManager
from domains.Student import Student
from domains.Course import Course
def compress_files():
    with ZipFile('students.dat', 'w') as z:
        z.write('students.txt')
        z.write('courses.txt')
        z.write('marks.txt')
def load_files():
    if os.path.exists('students.dat'):
        with ZipFile('students.dat', 'r') as z:
            z.extractall()  
        students = []
        with open('students.txt', 'r') as f:
            for line in f:
                student_id, name, gpa = line.strip().split(', ')
                students.append(Student(student_id, name, gpa))

        courses = []
        with open('courses.txt', 'r') as f:
            for line in f:
                course_id, name, credits = line.strip().split(', ')
                courses.append(Course(course_id, name, float(credits)))

        for student in students:
            student.marks = {}
            with open('marks.txt', 'r') as f:
                for line in f:
                    marks_student_id, marks = line.strip().split(': ', 1)
                    if marks_student_id == student.student_id:
                        student.marks = json.loads(marks)


        return students, courses
    return [], []

def main(stdscr):
    curses.cbreak()
    stdscr.clear()
    stdscr.refresh()
    students, courses = load_files()
    Inputmanager = InputManager(stdscr, students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr("HaiMinhs Student Management System\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. Display GPAs\n")
        stdscr.addstr("5. Display Marks\n")
        stdscr.addstr("6. Write to file\n")
        stdscr.addstr("7. Exit\n")
        stdscr.addstr("Choose an option: ")
        curses.echo()
        choice = int(stdscr.getstr().decode())

        if choice == 1:
            Inputmanager.input_students()
        elif choice == 2:
            Inputmanager.input_courses()
        elif choice == 3:
            Inputmanager.input_marks()
        elif choice == 4:
            OutputManager(stdscr, Inputmanager.students, Inputmanager.courses).display_gpas()
        elif choice == 5:
            OutputManager(stdscr, Inputmanager.students, Inputmanager.courses).display_marks()
        elif choice == 6:
            Inputmanager.write_data()
        elif choice == 7:
            compress_files()
            break
        
        else:
            stdscr.addstr("Invalid option.")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)