class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number_of_students(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            self.input_student_information()

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD/MM/YYYY): ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_number_of_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for _ in range(num_courses):
            self.input_course_information()

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses.append(course)

    def input_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID: ")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}) in {course_id}: "))
            student.marks[course_id] = mark

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks(self):
        self.list_courses()
        course_id = input("Select a course by ID to view marks: ")
        print(f"\nMarks for Course ID: {course_id}")
        for student in self.students:
            mark = student.marks.get(course_id, "No marks entered")
            print(f"{student.name} (ID: {student.student_id}): {mark}")

def main():
    smm = StudentMarkManagement()
    
    smm.input_number_of_students()
    smm.input_number_of_courses()
    smm.input_marks()
    
    smm.list_students()
    smm.show_student_marks()

if __name__ == "__main__":
    main()