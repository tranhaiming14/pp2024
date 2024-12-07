import curses
from input import InputManager
from output import OutputManager
from domains.Student import Student
from domains.Course import Course

def main(stdscr):
    curses.cbreak()
    stdscr.clear()
    stdscr.refresh()
    Inputmanager = InputManager(stdscr)

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
            break
        else:
            stdscr.addstr("Invalid option.")
            stdscr.refresh()
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)