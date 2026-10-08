from domains.student import Student
from domains.course import Course

def input_students(students):
    num = int(input("Enter number of students: "))
    for _ in range(num):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        students.append(Student(s_id, name, dob))
    print("-> Students added.")

def input_courses(courses):
    num = int(input("Enter number of courses: "))
    for _ in range(num):
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credits = int(input("Credits: "))
        courses.append(Course(c_id, name, credits))
    print("-> Courses added.")

def input_marks(courses, students, marks):
    c_id = input("Enter Course ID: ")
    course_exists = any(c.get_id() == c_id for c in courses)
    if not course_exists:
        print("Course ID does not exist!")
        return

    if c_id not in marks:
        marks[c_id] = {}

    for s in students:
        mark = float(input(f"Enter mark for {s.get_name()} ({s.get_id()}): "))
        marks[c_id][s.get_id()] = mark
    print("-> Marks recorded.")