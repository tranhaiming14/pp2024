def input_students():
    students = []
    student_num = int(input("Enter the number of students: "))
    for i in range(student_num):
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        DOB = input("Enter student's DOB: ")
        student = (name, student_id, DOB)
        students.append(student)
    return students
def input_courses():
    courses = []
    course_num = int(input("Enter the number of courses: "))
    for i in range(course_num):
        course_id = input("Enter the course ID: ")
        course_name = input("Enter coruse name: ")
        for course in courses:
            if course[0] == course_id:
                print("Course ID already exists")
                course_id = input("Enter the course ID: ")
        course = (course_id, course_name)
        courses.append(course)
    return courses
def input_marks(students, courses):
    marks = {}
    for course in courses:
        marks[course[1]] = {}
        for student in students:
            student_id = student[1] 
            cur_mark = float(input(f"Enter the mark of {student[0]} in course {course[1]}: "))
            marks[course[1]][student_id] = cur_mark
        return marks
def list_students(students):
    print("List of students: \n")
    for student in students:
        print(f"Name: {student[0]}, ID: {student[1]}, DOB: {student[2]} \n")
def list_courses(courses):
    print("List of courses: \n")
    for course in courses:
        print(f"Course name:  {course[1]}, ID: {course[0]}\n")
def list_marks(students, courses, marks):
    for course in courses:
        print(f"Marks of the course {course[1]}: \n")
        for student in students:
            print(f"Score in {course[1]} of student {student[0]} is:  {marks[course[1]][student[1]]}\n")
def student_management():
    students = input_students()
    courses = input_courses()
    marks = input_marks(students, courses)
    list_students(students)
    list_courses(courses)
    list_marks(students, courses, marks)
student_management()

    




