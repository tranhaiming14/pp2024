class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.marks = {}  

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
        course = Course(course_id, name)
        self.courses.append(course)

    def input_marks(self):
        for course in self.courses:
            print(f"Enter the mark for course {course.name}:")
            for student in self.students:
                mark = float(input(f"Enter the mark for student {student.name}: "))
                course.marks[student.student_id] = mark
    def display_marks(self):
        course_id = input("Enter the course ID to view marks: ")
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            for student in self.students:
                mark = course.marks.get(student.student_id, "No marks")
                print(f"Student {student.name} has {mark} in course {course_id}")
        else:
            print("Course not found.")

def main():
    manager = StudentManager()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()
    manager.display_marks()

if __name__ == "__main__":
    main()